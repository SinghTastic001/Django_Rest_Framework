from rest_framework import generics
from Bookapp.models import Author,Book
from .serializers import AuthorSerializer,BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['POST'])
def create_author(request):
    if request.method == "POST":
        # print(request.data)
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class BookDelete(generics.DestroyAPIView):
    # queryset and serializer-class are inbuilt label
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['DELETE'])
def AuthorDelete(request,pk):
    try:
        author = Author.objects.get(pk=pk)

    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="DELETE":
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)