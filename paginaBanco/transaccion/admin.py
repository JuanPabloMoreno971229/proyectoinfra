from django.contrib import admin
from .models import transaccion

# Register your models here.

class TransaccionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(transaccion, TransaccionAdmin)