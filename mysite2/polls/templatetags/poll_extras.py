from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

# @register.filter
@stringfilter
def kill(value, arg):
    return value.replace(arg, '')
register.filter('kill', kill)


@register.simple_tag
def print_something(s):
    return s + '疑是银河落九天'


from polls.models import Question

@register.inclusion_tag('results.html')
def show_results(pk):
    poll = Question.objects.get(pk=pk)
    choices = poll.choice_set.all()
    return {'choices': choices}
