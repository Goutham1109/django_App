from django.forms import ModelForm
from .models import TODO

class TodoCreateForm(ModelForm):
    class Meta:
        model= TODO
        fields = ['title','details','important']