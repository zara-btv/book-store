from django.urls import path
from .views import *
urlpatterns = [
    path('message/', get_data),
    path('Active/', active_library),
]
