
from .models import Books
from django.http import JsonResponse

def get_data(request):
    books=Books.objects.all().values(
        "id",
        "name",
        "year",
        "genres",
        "Age_group"
    )
    return JsonResponse(list(books), safe=False)

