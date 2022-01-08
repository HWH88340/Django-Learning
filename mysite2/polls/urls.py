from django.urls import path

from . import views

app_name = 'polls'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]



# http://127.0.0.0:8000/polls/34/
# url匹配捕获

# router : '' 不会匹配 GET 和 POST 参数或域名。 http://www.liujiangblog.com/polls/?page=3  GET POST
# view: views.index   HttpRequest对象