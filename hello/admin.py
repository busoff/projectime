from django.contrib import admin
from .models import Project, ProjectTimeEntry

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectTimeEntry)
