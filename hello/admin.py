from django.contrib import admin
from .models import Project, User, ProjectTimeEntry

# Register your models here.
admin.site.register(Project)
admin.site.register(User)
admin.site.register(ProjectTimeEntry)
