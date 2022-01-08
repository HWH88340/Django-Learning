from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from myform import ContactSearchForm
from models import Contact

# Create your views here.
def contact(request):
    t = loader.get_template("contact.html")
    c = Context({})
    if request.method == "POST":
        form = ContactSearchForm(request.POST)
        if form.is_valid():
            tmp = form.cleaned_data['name']
            result = Contact.objects.filter(name=tmp)
            c = Context({'searchname':tmp, 'result': result })

    return HttpResponse(t.render(c))
