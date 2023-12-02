# functions
from .models import Book
from .serializers import Bookserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def list_api_book(request):
    books=Book.objects.all()
    data=Bookserializers(books,many=True).data
    return Response({'data':data})

@api_view(['GET'])
def detail_api(request,pk):
    book=Book.objects.get(id=pk)
    data=Bookserializers(book).data
    return Response({'data':data})


# CREATE   API BY CLASS BASED VIEW
from rest_framework import generics

class List_Api(generics.ListAPIView):
        queryset=Book.objects.all()
        serializer_class=Bookserializers
        
class Detail_api(generics.RetrieveAPIView):
     queryset=Book.objects.all()
     serializer_class=Bookserializers
        

