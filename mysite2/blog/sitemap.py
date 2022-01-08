from django.contrib.sitemaps import Sitemap
from .models import Student
import datetime

class StudentSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5


    def items(self):
        return Student.objects.all()

    def lastmod(self,obj):
        return datetime.datetime.today()

    # def location(self,obj):
    #     return '/xxx/'

