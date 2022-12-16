from django.forms import ModelForm
from .models import Project


class Project_Form(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'