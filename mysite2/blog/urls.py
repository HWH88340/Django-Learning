from django.urls import path, register_converter

from . import views, converters
# from django.views.generic import TemplateView

app_name = 'blog'

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path("", views.paginated_blog),
    path('index/', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('goto/', views.goto),

    path('<int:id>/detail/', views.detail, name='detail'),
    path('<int:id>/man/', views.man, name='man'),
    path('<int:id>/woman/', views.woman, name='woman'),
    path('<yyyy:year>/', views.woman),
    path('about/', views.AboutView.as_view()),
]