from django.urls import path
from accounts.forms import VenueForm

from accounts.models import Venue
from . import views
urlpatterns = [
	path('', views.home),
	path('client_template/',views.client),
	path('add_venue/',views.VenueForm),
]