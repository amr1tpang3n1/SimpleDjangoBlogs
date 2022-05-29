from django.urls import path
from . import views

# url Configurations

urlpatterns = [
    path('', views.home_page)
]
