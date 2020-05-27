from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='tracker-home'),
    path('tracker/', views.tracker, name='tracker-logs'),
    path('stats/', views.stats, name='stats-logs'),
    path('ideas/', views.ideas, name='tracker-ideas'),
]
