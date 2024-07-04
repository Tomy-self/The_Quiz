from django.db import models

class Quiz(models.Model):
  quiz_title = models.CharField(max_length=200)
  quiz_creator = models.CharField(max_length=200)

  def __str__(self):
    return self.quiz_title

class Question(models.Model):
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  question_text = models.TextField()
  question_num = models.IntegerField(default=0)

  def __str__(self):
    return self.question_text

class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  answer_text = models.CharField(max_length=200)
  is_correct = models.BooleanField(default=False)

  def __str__(self):
    return self.answer_text