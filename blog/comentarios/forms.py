from django.forms import ModelForm
from .models import Comentario

class FormComantario(ModelForm):
    class Meta:
        model = Comentario
        fields = ("nome_comentario", "email_comentario", "comentario")