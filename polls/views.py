from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.
from django.template import loader

from .models import Choice, Question

# URLに対応づけてURLconfに反映させればブラウザで文字を表示
# def index(request):
#   return HttpResponse("Hello, world.　You're at the polls index.")

# 最新の5件の質問項目を表示
# def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   output = ', '.join([q.question_text for q in latest_question_list])
#   return HttpResponse(output)

# templateを利用　リスト形式になる
# def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   template = loader.get_template('polls/index.html')
#   context = {
#     'latest_question_list': latest_question_list,
#   }
#   return HttpResponse(template.render(context, request))

# ショートカット　loader, HttpResponseいらない
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {
    'latest_question_list': latest_question_list,
  }
  return render(request, 'polls/index.html', context)

# 質問詳細ページ
# def detail(request, question_id):
#   return HttpResponse("You're looking at question %s." % question_id)
#   # return HttpResponse("You're looking at question {}.".format(question_id))

# 指定された投票の質問文を表示
# def detail(request, question_id):
#   try:
#     question = Question.objects.get(pk=question_id)
#   except Question.DoesNotExist:
#     raise Http404("Question does not exist")
#   return render(request, 'polls/detail.html', {'question': question})

# ショートカット Http404
def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', { 'question':question })

def results(request, question_id): # 質問結果ページ
  # response = "You're looking at the results of question %s."
  # return HttpResponse(response % question_id)
  # detailとほぼ同じ
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id): # 投票ページ
  # ダミー実装
  # return HttpResponse("You're voting on question %s." % question_id)
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist): # 上のtryでPOSTデータにchoiceがない
    return render(request, 'polls/detail.html', { # エラーメッセージ付きの質問フォーム
      'question': question,
      'error_message': "You didn't select a choice",
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
