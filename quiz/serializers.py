from rest_framework.serializers import ModelSerializer

from .models import Quiz, Question, Subject


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ("name", )


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "question", "answer_a", "answer_b", "answer_c", "answer_d", )


class QuizSerializer(ModelSerializer):
    subject = SubjectSerializer(Subject.objects.all(), many=False)
    questions = QuestionSerializer(Question.objects.all(), many=True)
    class Meta:
        model = Quiz
        fields = ("id", "name", "subject", "questions", "count_questions", )
