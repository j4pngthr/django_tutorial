# URLに対応付け

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
  path('', views.index, name='index'), # viewとURLの対応付け
  # path('<int:question_id>/', views.detail, name='detail'),
  # path('<int:question_id>/results/', views.results, name='results'),
  # path('<int:question_id>/vote/', views.vote, name='vote'),
  # # path('specifics/<int:question_id>/', views.detail, name='detail'),
]
