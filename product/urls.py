from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path("", views.ProductList.as_view(), name="list"),
    path("detail", views.ProductDetail.as_view(), name="detail"),
    path("addcar/", views.ProductAddCar.as_view(), name="addcar"),
    path("removecar/", views.ProductRemoveCar.as_view(), name="removecar"),
    path("car/", views.ProductCar.as_view(), name="car"),
    path("finally/", views.ProductFinally.as_view(), name="finally"),
]
