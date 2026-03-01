from django.contrib import admin
from .models import Event,Booking
# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("event_name", "date", "time", "venue", "vacancy", "ratings","about_event","instructions","img_url")
    list_filter = ("date", "venue")
    list_display_links=("event_name", "date", "time", "venue", "vacancy", "ratings","about_event","instructions","img_url")
    search_fields = ("event_name", "venue")
    ordering = ("date", "time")   

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name","email","booked_at","event_id","event_name","event_date","event_time","event_img")
    list_filter = ("event_date",)
    list_display_links=("name","email","booked_at","event_id","event_name","event_date","event_time","event_img")
    search_fields = ("name",)
    # ordering = ("date", "time")   