from django.contrib import admin
from . import models





@admin.register(models.Stats)
class statsAdmin(admin.ModelAdmin):
    pass


