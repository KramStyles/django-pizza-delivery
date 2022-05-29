from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.OrderListCreateApiView.as_view(), name='order-list'),
]