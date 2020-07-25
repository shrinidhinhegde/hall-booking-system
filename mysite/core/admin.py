from django.contrib import admin
from .models import Booking

# Register your models here.
class AdminBooking(admin.ModelAdmin):
    list_display = ['hall1', 'hall2', 'date', 'ftime', 'ttime', 'purpose']

admin.site.register(Booking,AdminBooking)
