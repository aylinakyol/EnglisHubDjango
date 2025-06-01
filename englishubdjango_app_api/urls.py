from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from englishubdjango_app_api import views 

urlpatterns = [
    path('get-types/', views.get_types),
    path('get-levels/', views.get_levels),
    path('get-questions/', views.get_questions),
    path('get-options/', views.get_options),
]
