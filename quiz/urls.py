from django.urls import path

from .views import (
    get_all_quizzes,
    get_one_quiz,
    check,
    login,
)


urlpatterns = [
    path('login/', login, name="login"),
    path('', get_all_quizzes, name="quizzes"),
    path('quiz/<int:id>/', get_one_quiz, name="quiz"),
    path('quiz/<int:id>/check/', check, name="check"),
]