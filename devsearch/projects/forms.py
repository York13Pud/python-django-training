from django.forms import ModelForm
from django import forms
from .models import Project


class Project_Form(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "featured_image", "demo_link", "source_link", "tag"]
        widgets = {"tag": forms.CheckboxSelectMultiple()}
    
    def __init__(self, *args, **kwargs):
        super(Project_Form, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})