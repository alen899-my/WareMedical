from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("Doctor_name", "Specialization", "user")
    search_fields = ("Doctor_name", "Specialization", "user__username")
