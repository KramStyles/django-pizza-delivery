from django.urls import path

from . import views

urlpatterns = [
    path('register', views.CreateUserApiView.as_view(), name='hello-view'),
]
