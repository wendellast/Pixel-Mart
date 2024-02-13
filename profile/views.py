from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse


class ProfileCreate(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Profile Criar')

class ProfileUpdate(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Profile Update')

class ProfileLogin(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Profile Login')

class ProfileLogout(View):
    def get(self, *args, **kwargs):
        return  HttpResponse('Profile Logout')

