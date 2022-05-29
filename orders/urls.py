from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.OrderListCreateAPIView.as_view(), name='order-list'),
]