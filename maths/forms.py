from .models import Math
from django.forms import ModelForm


class MathForm(ModelForm):

    class Meta:
        model = Math
        fields = '__all__'
