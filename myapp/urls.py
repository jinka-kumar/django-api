from django.urls import path
from . import views

urlpatterns = [
    path('hi/', views.hi),
    path('hello/', views.hello),
]