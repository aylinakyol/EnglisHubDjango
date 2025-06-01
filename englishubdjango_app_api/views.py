from django.shortcuts import render # type: ignore
from django.http import JsonResponse # type: ignore
from englishubdjango_app_api.models import *
import traceback
from django.conf import settings # type: ignore
import json

def get_types(request):
    try:
        types = Type.objects.all()
        data = [
            {
                "id": type.id,
                "name": type.name,
            }
            for type in types
        ]
        return JsonResponse(data, safe=False)
    except Exception as e:
        # DEBUG modunda detaylı hata mesajı göster
        if settings.DEBUG:
            message = (
                f"***** ---> str(e): {str(e)} "
                f"***** ---> e.args: {str(e.args)} "
                f"***** ---> type(e): {type(e).__name__} "
                f"***** ---> traceback: {traceback.format_exc()}"
            )
        else:
            message = "An unexpected error occurred. Please contact support."
        return JsonResponse({"error": message}, status=500)
    
def get_levels(request):
    try:
        levels = Level.objects.all()
        data = [
            {
                "id": level.id,
                "name": level.name,
            }
            for level in levels
        ]
        return JsonResponse(data, safe=False)
    except Exception as e:
        # DEBUG modunda detaylı hata mesajı göster
        if settings.DEBUG:
            message = (
                f"***** ---> str(e): {str(e)} "
                f"***** ---> e.args: {str(e.args)} "
                f"***** ---> type(e): {type(e).__name__} "
                f"***** ---> traceback: {traceback.format_exc()}"
            )
        else:
            message = "An unexpected error occurred. Please contact support."
        return JsonResponse({"error": message}, status=500)

def get_questions(request):
    try:
        questions = Question.objects.all()
        data = [
            {
                "id": question.id,
                "description": question.description,
                "level": question.level.name,
            }
            for question in questions
        ]
        return JsonResponse(data, safe=False)
    except Exception as e:
        # DEBUG modunda detaylı hata mesajı göster
        if settings.DEBUG:
            message = (
                f"***** ---> str(e): {str(e)} "
                f"***** ---> e.args: {str(e.args)} "
                f"***** ---> type(e): {type(e).__name__} "
                f"***** ---> traceback: {traceback.format_exc()}"
            )
        else:
            message = "An unexpected error occurred. Please contact support."
        return JsonResponse({"error": message}, status=500)
    
def get_options(request):
    try:
        options = Option.objects.all()
        data = [
            {
                "id": option.id,
                "description": option.description,
                "question": option.question.description,
            }
            for option in options
        ]
        return JsonResponse(data, safe=False)
    except Exception as e:
        # DEBUG modunda detaylı hata mesajı göster
        if settings.DEBUG:
            message = (
                f"***** ---> str(e): {str(e)} "
                f"***** ---> e.args: {str(e.args)} "
                f"***** ---> type(e): {type(e).__name__} "
                f"***** ---> traceback: {traceback.format_exc()}"
            )
        else:
            message = "An unexpected error occurred. Please contact support."
        return JsonResponse({"error": message}, status=500)