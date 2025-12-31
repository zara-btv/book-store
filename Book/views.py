import datetime

from .models import Books
from django.http import JsonResponse ,HttpResponse
from  django.views.decorators.csrf import csrf_exempt
from .forms import CreateBook
import json
def get_data(request):
    books=Books.objects.all().values(
        "id",
        "name",
        "year",
        "genres",
        "Age_group"
    )
    return JsonResponse(list(books), safe=False)

def intro(request):
    html="welcome to my site"
    return HttpResponse(html)

# FOR GETTING BOOKS
#
# def get_all_books(request):
#     book_list=[]
#     books=Books.objects.all()
#     for book in books:
#         book_list.append({
#             'name':book.name
#         })

# def get_all_books(request):
#     books=list(Books.objects.all())
#     changed=json.dumps(books,default=str)
#     print(type(books))
#     print(type(changed))


#WRITE CRUD(CREATE READ UPDATE DELETE)
@csrf_exempt
def active_library(request):
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        body['year'] = datetime.datetime.now()
        form = CreateBook(body)
        if form.is_valid():
            book = form.save()
            return JsonResponse({'book_id':book.id})
    elif request.method == "GET":
        books = list(Books.objects.values())
        return JsonResponse(books, safe=False)
