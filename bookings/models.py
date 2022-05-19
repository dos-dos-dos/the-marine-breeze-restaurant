from django.db import models
from tables.models import Tables


class Bookings(models.Model):
    """
    Models for bookings 
    """
    BOOKING_STATUSES = (
        ('ACT', 'ACTIVE'),
        ('COMP', 'COMPLETE'),
        ('CANC', 'CANCELLED'),
        ('CANC', 'CANCELLED'),
        ('NOSHO', 'NO_SHOW'),
    )  

    booking_ref = models.IntegerField(primary_key=False)
    booking_created = models.DateField(auto_now_add=True)
    booking_start = models.DateTimeField()
    booking_end = models.DateTimeField()
    booking_status = models.CharField(max_length=5, choices=BOOKING_STATUSES, default="Active")
    table_no =  models.ForeignKey(Tables, on_delete=models.CASCADE)
    booking_date = models.DateField()
    customer = models.CharField(max_length=10)
    booked_by = models.CharField(max_length=10)

