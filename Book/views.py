import datetime
from django.shortcuts import render
from .models import Books
from django.http import JsonResponse ,HttpResponse
from  django.views.decorators.csrf import csrf_exempt
from .forms import CreateBook
import json
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.views import APIView
def get_data(request):
    books=Books.objects.all().values(
        "id",
        "name",
        "year",
        "genres",
        "Age_group"
    )
    return JsonResponse(list(books), safe=False)


def list_books(request):
    books = Books.objects.all()
    return render(request, 'myapp/list.html', {'books': books})

def home(request):
    return render (request, "myapp/index.html")


@csrf_exempt
def active_library(request):
    if request.method == "GET":
        books = list(Books.objects.values())
        return JsonResponse(books, safe=False)
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
#@csrf_exempt
# def Edit_library(request):
#     if request.method == "POST":
#         body = json.loads(request.body.decode('utf-8'))
#         body['year'] = datetime.datetime.now()
#         form = CreateBook(body)
#         if form.is_valid():
#             book = form.save()
#             return JsonResponse({'book_id':book.id})
#     elif request.method == "GET":
#         books = list(Books.objects.values())
#         return JsonResponse(books, safe=False)

class BookView(APIView):
    def post(self,request):
        body = json.loads(request.body.decode('utf-8'))
        form = BookSerializer(data=body)
        print(body)
        if form.is_valid():
            book = form.save()
            return JsonResponse({'book_id': book.id})
    def get(self,request):
        books = list(Books.objects.values())
        return JsonResponse(books, safe=False)


class BookGenericAPI(generics.ListCreateAPIView):

    serializer_class = BookSerializer
    queryset = Books.objects.all()

class BookChangeAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Books.objects.all()
