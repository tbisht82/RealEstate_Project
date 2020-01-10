from django.contrib import admin
from .models import Realtor

class RealtorgAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')


# Register your models here.
admin.site.register(Realtor,RealtorgAdmin)
