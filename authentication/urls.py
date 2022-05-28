from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.HelloAuthView.as_view(), name='hello-view'),
]
