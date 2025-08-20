from django.contrib import admin
from .models import Receptionist
@admin.register(Receptionist)

class ReceptionistAdmin(admin.ModelAdmin):
    list_display=('Receptionist_name','user')
# Register your models here.
