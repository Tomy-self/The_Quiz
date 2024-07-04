from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('create/', views.create_quiz, name='create_quiz'),
  path('<int:quiz_id>/create/question/', views.create_question, name='create_question'),
  path('<int:question_id>/create/answer', views.create_answer, name='create_answer'),
]