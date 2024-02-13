from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.OrderBuy.as_view(), name="buy"),
    path('close/', views.OrderClose.as_view(), name="close"),
    path('detail/',  views.OrderDetail.as_view(), name="detail"),
]

