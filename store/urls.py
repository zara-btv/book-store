
from django.contrib import admin
from django.urls import path, include
from Book.views import intro
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', intro),
    path('book/', include('Book.urls'))
]
