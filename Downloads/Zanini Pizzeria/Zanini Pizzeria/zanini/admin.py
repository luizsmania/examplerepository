from django.contrib import admin
from .models import Table, Reservation

# Register your models here.
@admin.register(Table, Reservation)
class TableAdmin(admin.ModelAdmin):
    pass
