from django.forms import ModelForm
from .models import *


class Addquestionform(ModelForm):
    class Meta:
        model = Quesmodel
        fields = "__all__"