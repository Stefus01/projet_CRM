from django.urls import path
from . import views
urlpatterns = [
	path('', views.home),
	path('client_template/',views.client,name='client'),
	path('add_venue/',views.add_venue,name='add-venue'),
]