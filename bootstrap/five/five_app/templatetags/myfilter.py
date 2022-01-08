from django import template

register = template.Library()

def myfilter(mylist):
    res = []
    for val in mylist:
        if val >= 5 and val <= 10:
            res.append(val)

    return res

register.filter(myfilter)
