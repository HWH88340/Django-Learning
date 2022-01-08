from django.urls import path
from login import views

urlpatterns = [
    path('drive_car/', views.drive_car),
    path('login/',views.login),
    path('logout/',views.logout),
]