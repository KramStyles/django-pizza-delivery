from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.OrderListCreateAPIView.as_view(), name='order-list'),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('<int:pk>/status/', views.OrderStatusUpdateAPIView.as_view(), name='order-status'),
    path('<user_id>/orders', views.UserOrderView.as_view(), name='user-order'),
    path('<user_id>/orders/<order_id>', views.UserOrderDetailView.as_view(), name='user-specific-order'),
]
