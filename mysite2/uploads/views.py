from django.shortcuts import render
from .models import User
# Create your views here.
from .forms import FileFieldForm
from django.conf import settings

def add(request):
    if request.method == "POST":
        name = request.POST.get('username')
        img = request.FILES.get('img')
        introduce = request.FILES.get('introduce')
        print(name, img, introduce)
        user = User(name=name, img=img, introduce=introduce)
        user.save()
    return render(request, 'uploads/add.html', locals())


def multiple_upload(request):
    # request.upload_handlers.insert(0, ProgressBarUploadHandle(request))
    if request.method == "POST":
        form = FileFieldForm()
        files = request.FILES.getlist('file_field')
        print(files)
        for f in files:
            file_path = settings.MEDIA_ROOT / f.name
            with open(file_path, 'wb') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
    else:
        form = FileFieldForm()
    return render(request, 'uploads/multiple_upload.html', {'form':form})



# 1. /index/  2. /static/...  3. /media/1.jpg
def detail(request):
    user_list = User.objects.all()
    return render(request, 'uploads/detail.html', locals())