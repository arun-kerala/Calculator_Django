from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('answer/', views.submit_answer, name='answer'),
    path('history/', views.history, name='history'),
    path('clear_history/', views.clear_history, name='clear_history')
]
