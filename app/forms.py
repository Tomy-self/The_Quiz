from django import forms
from .models import Quiz, Question, Answer

class QuizForm(forms.ModelForm):
  class Meta:
    model = Quiz
    fields = ['quiz_title', 'quiz_creator']

class QuestionForm(forms.ModelForm):
  class Meta:
    model = Question
    fields = ['quiz', 'question_text', 'question_num']

class AnswerForm(forms.ModelForm):
  class Meta:
    model = Answer
    fields = ['question', 'answer_text', 'is_correct']