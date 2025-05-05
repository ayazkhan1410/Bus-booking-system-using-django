from django.urls import path
from .views import *


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contact-us/", ContactUsView.as_view(), name="contact_us"),
    path("search-results/", SearchResultsView.as_view(), name="search_results"),
    path("bus-details/", BusDetailsView.as_view(), name="bus_details"),
    path("booking-history/", BookingHistoryView.as_view(), name="booking_history"),
    path("booking-success/", BookingSuccessView.as_view(), name="booking_success"),
    path("booking-failed/", BookingFailedView.as_view(), name="booking_failed"),

    # Authentication URLs
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),

]
