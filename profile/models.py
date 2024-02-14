from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from utils.tools import valida_cpf

import re


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    birth_date = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    city = models.CharField(max_length=50)
    state = models.CharField(
        max_length=2,
        default="BA",
        choices=(
            ("AC", "Acre"),
            ("AL", "Alagoas"),
            ("AP", "Amapá"),
            ("AM", "Amazonas"),
            ("BA", "Bahia"),
            ("CE", "Ceará"),
            ("DF", "Distrito Federal"),
            ("ES", "Espírito Santo"),
            ("GO", "Goiás"),
            ("MA", "Maranhão"),
            ("MT", "Mato Grosso"),
            ("MS", "Mato Grosso do Sul"),
            ("MG", "Minas Gerais"),
            ("PA", "Pará"),
            ("PB", "Paraíba"),
            ("PR", "Paraná"),
            ("PE", "Pernambuco"),
            ("PI", "Piauí"),
            ("RJ", "Rio de Janeiro"),
            ("RN", "Rio Grande do Norte"),
            ("RS", "Rio Grande do Sul"),
            ("RO", "Rondônia"),
            ("RR", "Roraima"),
            ("SC", "Santa Catarina"),
            ("SP", "São Paulo"),
            ("SE", "Sergipe"),
            ("TO", "Tocantins"),
        ),
    )

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        return self.user.username

    def clean(self):
        error_messagens = {}

        if not valida_cpf(self.cpf):
            error_messagens["cpf"] = "Digite um 'CPF' válido"

        if re.search(r"[0-9]", self.cep) or len(self.cep < 8):
            error_messagens["cep"] = "Digite um 'CEP' válido"

        if error_messagens:
            raise ValidationError(error_messagens)
