from django.http import HttpRequest
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Question, Quiz, Result
from .serializers import QuizSerializer


@api_view(http_method_names=["GET"])
@permission_classes(permission_classes=[IsAuthenticated])
@authentication_classes(authentication_classes=[TokenAuthentication])
def get_all_quizzes(request: HttpRequest):
    quizzes_queryset = Quiz.objects.all()
    quizzes = QuizSerializer(quizzes_queryset, many=True).data
    return Response(quizzes)


@api_view(http_method_names=["GET"])
@permission_classes(permission_classes=[IsAuthenticated])
@authentication_classes(authentication_classes=[TokenAuthentication])
def get_one_quiz(request: HttpRequest, id: int):
    quiz_queryset = get_object_or_404(Quiz, pk=id)
    quiz = QuizSerializer(quiz_queryset, many=False).data
    return Response(quiz)


@api_view(http_method_names=["POST"])
@permission_classes(permission_classes=[IsAuthenticated])
@authentication_classes(authentication_classes=[TokenAuthentication])
def check(request: HttpRequest, id: int):
    quiz = get_object_or_404(Quiz, pk=id)
    answers = request.data.get("answers")
    all = 0
    count = 0
    d = {}
    for question, j in zip(quiz.questions.all(), answers):
        print(question.correct, answers[j])
        if (question.correct == answers[j]):
            count += 1
            d[all] = "correct"
        else:
            d[all] = "incorrect"
        all += 1
    result = Result.objects.create(
        author=request.user,
        quiz=quiz,
        score=((count / all) * 100),
        json=d,
    )
    return Response({
        "score": ((count / all) * 100),
        "json": d
    })

@api_view(http_method_names=["POST"])
def login(request: HttpRequest):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)
    if not user:
        return Response({
            "error": "User not found",
        })
    token = Token.objects.filter(user=user)
    if token:
        token = token.first()
    else:
        token = Token.objects.create(user=user)
    return Response({
        "error": None,
        "token": str(token),
    })