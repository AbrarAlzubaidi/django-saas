from django.urls import path
from .views import all_visits

urlpatterns = [
    path('', all_visits),
    
]