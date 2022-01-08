from django.shortcuts import render, HttpResponse
from django.core import management
from django.contrib import messages
from django.conf import global_settings
# Create your views here.


# root_logger = logging.getLogger(__name__)
import logging
my_logger = logging.getLogger('my')
# django_logger = logging.getLogger('django')


class Start_with_django(logging.Filter):
    def filter(self, record):
        if record.msg.startswith('django'):
            return True
        else:
            return False


def mid_test(request):
    # print('执行视图mid_test')
    # print('当前用户：%s' % request.user)
    # messages.add_message(request, messages.INFO, '这是来自mid_test视图的问候')
    # root_logger.error('这是来自mid_test的错误日志')
    my_logger.error('这是来自my记录器的日志')
    my_logger.info('这是来自my记录器的日志')
    my_logger.info('django这是来自my记录器的日志')
    # django_logger.info('....')

    # raise
    # management.call_command('dumpdata', 'app.book')

    return HttpResponse('200,ok')

def template_test(request):
    import datetime
    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(days=1)
    lis = range(10)
    outer = range(4)
    time = datetime.datetime.now() - datetime.timedelta(minutes=2)
    return render(request, 'template_test.html', locals())