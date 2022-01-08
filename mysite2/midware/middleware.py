from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


# class Md1(MiddlewareMixin):
#
#     def process_request(self,request):
#         print("Md1处理请求")
#
#     def process_response(self,request,response):
#         print("Md1返回响应")
#         return response
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#
#         print("Md1在执行%s视图前" % view_func.__name__)
#
#     def process_exception(self,request,exception):
#         print("Md1处理视图异常...")
#
#
#
# class Md2(MiddlewareMixin):
#
#     def process_request(self,request):
#         print("Md2处理请求")
#
#     def process_response(self,request,response):
#         print("Md2返回响应")
#         return response
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#
#         print("Md2在执行%s视图前" % view_func.__name__)
#
#     def process_exception(self,request,exception):
#         print("Md2处理视图异常...")

class Md1:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        print("Md1处理请求")

        response = self.get_response(request)

        print("Md1返回响应")

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        print("Md1在执行%s视图前" %view_func.__name__)

    def process_exception(self,request,exception):
        print("Md1处理视图异常...")


class Md2:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Md2处理请求")

        response = self.get_response(request)

        print("Md2返回响应")

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("Md2在执行%s视图前" % view_func.__name__)

    def process_exception(self, request, exception):
        print("Md2处理视图异常...")



from django.http import HttpResponseForbidden
class BlackListMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.META['REMOTE_ADDR'] in getattr(settings, 'BLACK_LIST', []):
            return HttpResponseForbidden('<h1>对不起，你的IP不可以访问服务器。</h1>')

        response = self.get_response(request)

        return response

import sys
from django.views.debug import technical_500_response
class DebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if request.user.is_superuser or request.META.get('REMOTE_ADDR') in settings.ADMIN_IP:
            return technical_500_response(request, *sys.exc_info())


import pytz
from django.utils import timezone


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get('django-timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()

        response = self.get_response(request)

        return response
