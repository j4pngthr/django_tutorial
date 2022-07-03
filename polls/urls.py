# URLに対応付け

from django.urls import path

from . import views

app_name = 'polls' # pollsアプリの名前空間をURLconfに追加
urlpatterns = [ # viewとURLの対応付け
  # path('', views.index, name='index'), # index
  # path('<int:question_id>/', views.detail, name='detail'), # detail
  # path('<int:question_id>/results/', views.results, name='results'), # results
  # path('<int:question_id>/vote/', views.vote, name='vote'), # vote

  # path('specifics/<int:question_id>/', views.detail, name='detail'),

  path('', views.IndexView.as_view(), name='index'),
  path('<int:pk>/', views.DetailView.as_view(), name='detail'),
  path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
  path('<int:question_id>/vote/', views.vote, name='vote'),
]
