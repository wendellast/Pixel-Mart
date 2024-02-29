from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse

from . import models
from . import forms

class ProfileBase(View):
    template_name = 'profile/create.html'
    
    def setup(self, *args, **kwargs):
        super().setup(**args, **kwargs)
        
        self.context = {
            'userform': forms.Userform(
                data=self.resquest.POST or None
            ),
            
            'perfilform': forms.PerfilForm(
                data=self.request.POST or None
            )
        }
        
        self.render = render(self.request, self.template_name, self.context)
        
    
    def get(self, *args, **kwargs):
        return self.render


class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Profile Update")


class ProfileLogin(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Profile Login")


class ProfileLogout(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Profile Logout")
