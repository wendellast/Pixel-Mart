from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models


class ProductList(ListView):
    model = models.Product
    template_name = "product/list.html"
    context_object_name = "products"


class ProductDetail(ListView):
    model = models.Product
    template_name = "product/product_detail.html"
    context_object_name = "products"


class ProductAddCar(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Product add Car")


class ProductRemoveCar(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Product Remove car")


class ProductCar(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Product Car")


class ProductFinally(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Product finaly")
