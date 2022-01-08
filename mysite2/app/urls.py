from django.urls import path
from . import views


urlpatterns = [
    path('current_datetime/', views.current_datetime),
    path('my_view/', views.my_view),
    path('detail/', views.detail),
    path('print/', views.print_request),
    path('index/', views.index),
]

