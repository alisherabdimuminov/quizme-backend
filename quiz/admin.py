from django.contrib import admin

from .models import Question, Subject, Quiz, Result


@admin.register(Quiz)
class QuizModelAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Subject)
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ["question", "correct"]


@admin.register(Result)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ["author", "score"]