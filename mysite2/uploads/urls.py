from django.urls import path
from . import views

app_name = 'uploads'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('detail/', views.detail, name='detail'),
    path('multiple_upload/', views.multiple_upload),
]