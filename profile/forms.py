from django.contrib.auth.models import User
from django import forms
from . import models


class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = "__all__"
        exclude = ("user",)


class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,  # tornando a senha obrigatória
        widget=forms.PasswordInput(),
    )

    password_confirm = forms.CharField(
        required=False, widget=forms.PasswordInput()  # tornando a senha obrigatória
    )

    def __init__(self, user_form=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_form = user_form

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password",
            "password_confirm",
            "email",
        )

    def clean(self):
        cleaned_data = super().clean()
        validation_error_msg = {}

        user_data = cleaned_data.get("username")
        password_data = cleaned_data.get("password")
        password_confirm_data = cleaned_data.get("password_confirm")
        email_data = cleaned_data.get("email")

        user_db = User.objects.filter(username=user_data).filter()
        # password_db = User.objects.filter(username=password_data).filter()
        # passowrd_confirm_db = User.objects.filter(username=password_confirm_data).filter()
        email_db = User.objects.filter(username=email_data).filter()

        erro_msg_username = "Usuario ja existe"
        erro_msg_email = "email ja existe"
        erro_msg_password = "As senhas sao diferentes"
        erro_msg_password_short = " A senha é muito curta"
        error_msg_exist = "Esse endereço ja existe"
        error_msg_required = "Este campo é obrigatório."

        if self.user_form:
            if user_db:
                if user_data != user_data.username:
                    validation_error_msg["username"] = error_msg_exist

            if email_db:
                if email_data != email_db.email:
                    validation_error_msg["email"] = error_msg_exist

            if password_data:
                if password_data != password_confirm_data:
                    validation_error_msg["password"] = erro_msg_password
                    validation_error_msg["password_confirm"] = erro_msg_password

                if len(password_data) < 6:
                    validation_error_msg["password"] = erro_msg_password_short
        else:
            if user_db:
                validation_error_msg["username"] = error_msg_exist

            if email_db:
                validation_error_msg["email"] = error_msg_exist

            if not password_data:
                validation_error_msg["password"] = error_msg_required

            if not password_confirm_data:
                validation_error_msg["password_confirm"] = error_msg_required

            if password_data != password_confirm_data:
                validation_error_msg["password"] = erro_msg_password
                validation_error_msg["password_confirm"] = erro_msg_password

            if len(password_data) < 6:
                validation_error_msg["password"] = erro_msg_password_short

        if validation_error_msg:
            raise (forms.ValidationError(validation_error_msg))

        return cleaned_data
