from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from app import views
from midware.views import mid_test, template_test
from django.contrib.sitemaps.views import sitemap
# from blog.sitemap import StudentSitemap
from django.contrib.sitemaps import GenericSitemap
from blog.models import Student

info_dict = {
    'queryset': Student.objects.all(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('uploads/', include('uploads.urls')),
    path('blog/', include('blog.urls')),
    path('author/', include('blog.urls', namespace='blog_author')),
    path('publisher/', include('blog.urls', namespace='blog_publisher')),
    path('app/', include('app.urls')),
    path('books/', include('books.urls')),
    path('midtest/', mid_test),
    path('template/', template_test),
    path('your_name/', views.get_name),
    path('add_author/', views.add_author),
    path('signal/', views.create_signal),
    path('timezone/', views.set_timezone),
    path('which_site/', views.which_site),
    path('login/', include('login.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('pages/', include('django.contrib.flatpages.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': {'blog':GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 增加的条目
handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.error

# from django.urls import re_path
# from django.views.static import serve
#
# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT
#         }),
#     ]