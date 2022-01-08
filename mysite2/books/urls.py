from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('publishers/', views.PublisherList.as_view(), name='publisher_list'),
    path('publishers/<int:pk>/', views.PublisherDetail.as_view()),
    path('books_of_machine/', views.MachineBookList.as_view()),
    path('books/<publisher>/', views.PublisherBookList.as_view()),
    path('authors/add/', views.AuthorCreate.as_view(), name='author-add'),
    path('authors/<int:pk>/', views.AuthorUpdate.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
    path('authors/<int:pk>/detail/', views.AuthorDetailView.as_view(), name='author-detail'),
]

