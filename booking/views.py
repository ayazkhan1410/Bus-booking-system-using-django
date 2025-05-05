from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


class ContactUsView(View):
    def get(self, request):
        return render(request, "contact.html")


class SearchResultsView(View):
    def get(self, request):
        return render(request, "search_result.html")


class BusDetailsView(View):
    def get(self, request):
        return render(request, "bus_details.html")


class BookingHistoryView(View):
    def get(self, request):
        return render(request, "booking_history.html")


class BookingSuccessView(View):
    def get(self, request):
        return render(request, "booking_success.html")


class BookingFailedView(View):
    def get(self, request):
        return render(request, "booking_failed.html")

    def post(self, request):
        return HttpResponse("Booking failed, please try again.")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        return HttpResponse("Registration successful!")


class LogoutView(View):
    def get(self, request):
        return HttpResponse("You have been logged out.")
