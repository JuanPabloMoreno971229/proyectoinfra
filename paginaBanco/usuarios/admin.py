from django.contrib import admin
from .models import usuario

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(usuario, UsuarioAdmin)