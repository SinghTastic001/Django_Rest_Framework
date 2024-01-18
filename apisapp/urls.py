from django.urls import path
from .views import AuthorList,BookList,create_author,BookDelete,AuthorDelete


urlpatterns = [
    path('author_list/',AuthorList.as_view(),name='author_list'),
    path('book_list/',BookList.as_view(),name='book_list'),
    path('create_author/',create_author,name='create_author'),
    path('book_delete/<int:pk>/',BookDelete.as_view(),name='book_delete'),
    path('author_delete/<int:pk>/',AuthorDelete,name='author_delete'),
]