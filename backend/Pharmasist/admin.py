from django.contrib import admin
from .models import Pharmasist
# Register your models here.

@admin.register(Pharmasist)
class PharmasistAdmin(admin.ModelAdmin):
    list_display=('pharmasist_name','user')
    search_fields=('pharmasist_name','user__username')