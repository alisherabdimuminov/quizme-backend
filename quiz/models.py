from django.db import models
from django.contrib.auth.models import User


def default():
    return {}

class Question(models.Model):
    question = models.TextField()
    answer_a = models.TextField()
    answer_b = models.TextField()
    answer_c = models.TextField()
    answer_d = models.TextField()
    correct = models.TextField()

    def __str__(self):
        return self.question[:5:]
    
    
class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, related_name="quiz_questions")

    def __str__(self):
        return self.name
    
    def count_questions(self):
        return self.questions.count()
    

class Result(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    json = models.JSONField(null=True, blank=True, default=default)

    def __str__(self):
        return str(self.score)
