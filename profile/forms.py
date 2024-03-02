from django.contrib.auth.models import User
from django import forms
from . import models

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = '__all__'
        exclude = ('user',)

class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,  # tornando a senha obrigatória
        widget=forms.PasswordInput()
    )

    def __init__(self, user_form=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_form = user_form

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')

    def clean(self):
        cleaned_data = super().clean()
        validation_error_msg = {

        }

        if self.user_form:
            print("OLÀAA")
        else:
            validation_error_msg["username"] = 'aaaaaaaaa'

        if validation_error_msg:
            raise(forms.ValidationError(validation_error_msg))

        return cleaned_data
