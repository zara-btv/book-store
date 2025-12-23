from django.urls import path
from .views import get_data
urlpatterns = [
    path('message/', get_data),
]
