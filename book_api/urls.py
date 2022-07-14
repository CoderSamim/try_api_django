from django.urls import path

from book_api.views import book_list ,book_create, book ##import view

urlpatterns=[
    
    path('',book_create),
    path('list/',book_list),
     path('<int:pk>',book)
    
]
