from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class ProductList(ListView):
    def get(self, *args, **kwargs):
        return  HttpResponse('Product Lista')

class ProductDetail(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Product Detail')

class ProductAddCar(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Product add Car')

class ProductRemoveCar(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Product Remove car')

class ProductCar(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Product Car')

class ProductFinally(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Product finaly')
