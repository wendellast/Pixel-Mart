from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse


class OrderBuy(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Order Compra")


class OrderClose(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Order Close")


class OrderDetail(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Order Detail")
