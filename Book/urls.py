from django.urls import path
from .views import *
from .views import BookGenericAPI

urlpatterns = [
    path('', home, name='home'),
    path('view-books/', list_books, name='view-books'),
    path('active/', active_library, name='active'),
    path('create', BookView.as_view()),
    path('book-generic', BookGenericAPI.as_view()),
    path('change/<int:pk>/update',BookChangeAPI.as_view())
]