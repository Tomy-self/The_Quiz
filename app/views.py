from django.shortcuts import render, redirect
from .forms import QuizForm, QuestionForm, AnswerForm

def index(request):
  return render(request, 'app/index.html')

def create_quiz(request):
  if request.method == 'POST':
    quiz_form = QuizForm(request.POST)
    if quiz_form.is_valid():
      quiz = quiz_form.save()  # 퀴즈 저장
      return redirect('create_question', quiz_id=quiz.id)
  else:
    quiz_form = QuizForm()
  return render(request, 'app/create_quiz.html', {'quiz_form': quiz_form})

def create_question(request, quiz_id):
  if request.method == 'POST':
    question_form = QuestionForm(request.POST)
    if question_form.is_valid():
      question = question_form.save(commit=False)
      question.quiz_id = quiz_id
      question.save()
      return redirect('create_answer', question_id=question.id)
  else:
    question_form = QuestionForm()
  return render(request, 'app/create_question.html', {'question_form': question_form})

def create_answer(request, question_id):
  if request.method == 'POST':
    answer_form = AnswerForm(request.POST)
    if answer_form.is_valid():
      answer_form.save()
      return redirect('create_answer', question_id=question_id)
  else:
    initial_data = {'question': question_id}
    answer_form = AnswerForm(initial=initial_data)
  return render(request, 'app/create_answer.html', {'answer_form': answer_form})