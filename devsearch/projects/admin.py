from django.contrib import admin

from .models import Project, Review, Tag

# Register the models here.
admin.site.register(model_or_iterable = Project)
admin.site.register(model_or_iterable = Review)
admin.site.register(model_or_iterable = Tag)