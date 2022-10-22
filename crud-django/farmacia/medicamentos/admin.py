from django.contrib import admin
from medicamentos.models import Remedio
# Register your models here.

class RemedioAdmin (admin.ModelAdmin):
    list_display=['codigo','nombre','precio','laboratorio','fechaIngreso']


admin.site.register(Remedio,RemedioAdmin)