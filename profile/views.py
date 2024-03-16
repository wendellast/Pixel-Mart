from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse

from . import models
from . import forms


class ProfileBase(View):
    template_name = "profile/register_user.html"

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if self.request.user.is_authenticated:
            self.context = {
                "userform": forms.UserForm(
                    data=self.request.POST or None,
                    user_form=self.request.user,
                    instance=self.request.user,
                ),
                "perfilform": forms.PerfilForm(
                    data=self.request.POST or None,
                ),
            }

        else:
            self.context = {
                "userform": forms.UserForm(
                    data=self.request.POST or None,
                ),
                "perfilform": forms.PerfilForm(data=self.request.POST or None),
            }

        self.render = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):
        return self.render


class ProfileCreate(ProfileBase):
    def post(self, *args, **kwargs):
        return self.render


class ProfileUpdate(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Profile Update")


class ProfileLogin(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Profile Login")


class ProfileLogout(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Profile Logout")
