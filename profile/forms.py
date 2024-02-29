from django.contrib.auth.models import User
from django import forms
from . import models

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = '__all__'
        exclude = ('user',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')
        
        
    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data