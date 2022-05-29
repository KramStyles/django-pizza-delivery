from django.urls import path

from . import views

urlpatterns = [
    path('order/', views.OrderListCreateApiView.as_view(), name='order-list'),
]