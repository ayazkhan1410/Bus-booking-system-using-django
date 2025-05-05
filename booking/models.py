from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .helpers import MyUserManager
from .booking_status import BOOKING_STATUS


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Route(models.Model):
    route_name = models.CharField(max_length=100, null=True, blank=True)
    route_number = models.CharField(max_length=100, null=True, blank=True)
    route_distance = models.IntegerField(null=True, blank=True)
    route_duration = models.IntegerField(null=True, blank=True)
    route_fare = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class Bus(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, null=True, blank=True)
    bus_name = models.CharField(max_length=100, null=True, blank=True)
    bus_number = models.CharField(max_length=100, null=True, blank=True)
    seats_capacity = models.IntegerField(null=True, blank=True)
    departure_time = models.TimeField(null=True, blank=True)
    arrival_time = models.TimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available_seats = models.IntegerField(null=True, blank=True)
    bus_image = models.ImageField(upload_to='buses/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Booking(models.Model):
    booking_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    total_passengers = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_status = models.CharField(max_length=100, choices=BOOKING_STATUS)
    booking_amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_seats = models.IntegerField()
    from_location = models.CharField(max_length=100, null=True, blank=True)
    to_location = models.CharField(max_length=100, null=True, blank=True)
    arrival_time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BookigHistory(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    contact_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    feedback_date = models.DateTimeField(auto_now_add=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
