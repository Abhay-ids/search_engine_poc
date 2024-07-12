from django.urls import path
from . import views

urlpatterns = [
    path('', views.import_site, name='import_site'),
    # Other paths if needed
]