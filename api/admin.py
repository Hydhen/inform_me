from django.contrib import admin

# Register your models here.
from .models import Domain, Role, Staff, Status, Project, Comment

admin.site.register(Domain)
admin.site.register(Role)
admin.site.register(Staff)
admin.site.register(Status)
admin.site.register(Project)
admin.site.register(Comment)
