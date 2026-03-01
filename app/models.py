from django.db import models

# Create your models here.
class registerdetails(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=14)
    c_password=models.CharField(max_length=14)
    def __str__(self):
        return self.name
    
class Event(models.Model):
    event_name = models.CharField(max_length=255)
    about_event = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=255)
    instructions = models.TextField(blank=True, null=True)
    vacancy = models.PositiveIntegerField()
    ratings = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    img_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.event_name
    
from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    event_id = models.IntegerField()  # store Event.id manually
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_img = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.event_name}"
