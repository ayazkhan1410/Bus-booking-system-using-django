from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    MyUser, Route, Bus, Booking, BookigHistory,
    ContactUs, Feedback
)


@admin.register(MyUser)
class MyUserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'is_admin', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)
    list_filter = ('is_admin', 'is_active')
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'username',
                    'password1',
                    'password2',
                    'is_admin',
                    'is_active',
                ),
            },
        ),
    )


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_name', 'route_number', 'route_distance', 'route_duration', 'route_fare')
    search_fields = ('route_name', 'route_number')
    list_filter = ('route_name',)


@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = (
        'bus_name', 'bus_number', 'route', 'departure_time', 'arrival_time',
        'seats_capacity', 'available_seats', 'price'
    )
    search_fields = ('bus_name', 'bus_number')
    list_filter = ('route',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'booking_id', 'bus', 'user', 'total_passengers', 'booking_status',
        'booking_amount', 'booking_seats', 'from_location', 'to_location',
        'arrival_time', 'booking_date', 'created_at', 'updated_at',
    )
    search_fields = ('booking_id', 'user__email', 'bus__bus_number')
    list_filter = ('booking_status', 'booking_date')
    readonly_fields = ('created_at', 'updated_at', 'booking_date')


@admin.register(BookigHistory)
class BookingHistoryAdmin(admin.ModelAdmin):
    list_display = ('booking', 'user')
    search_fields = ('booking__booking_id', 'user__email')


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'contact_date')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at', 'updated_at', 'contact_date')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'feedback_date')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at', 'updated_at', 'feedback_date')
