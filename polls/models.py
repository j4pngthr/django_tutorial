import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model): # 投票項目
  question_text = models.CharField(max_length=200) # 質問事項
  pub_date = models.DateTimeField('date published') # 公開日 # オプションでフィールド名
  def __str__(self): # shellで表示させるときわかりやすい文字列に
    return self.question_text
  def was_published_recently(self):
    return self.pub_date >= timezone.now()- datetime.timedelta(days=1)

class Choice(models.Model): # 投票項目に対する選択肢
  question = models.ForeignKey(Question, on_delete=models.CASCADE) # Question関数と紐付け # CASCADE:Questionが消えたら紐づいてるChoiceも消える
  choice_text = models.CharField(max_length=200) # 選択肢のテキスト
  votes = models.IntegerField(default=0) # 投票数
  def __str__(self): # shellで表示させるときわかりやすい文字列に
    return self.choice_text
