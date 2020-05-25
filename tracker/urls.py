from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='tracker-home'),
    path('tracker/', views.tracker, name='tracker-logs'),
]
