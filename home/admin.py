from django.contrib import admin

from .models import Domain, Role, Staff

admin.site.register(Domain)
admin.site.register(Role)
admin.site.register(Staff)
