from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publisher, Book, Author
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
# Create your views here.


class PublisherList(ListView):
    # model = Publisher
    queryset = Publisher.objects.order_by('name')
    context_object_name = 'publishers'


class PublisherDetail(DetailView):
    # model = Publisher
    queryset = Publisher.objects.all()
    context_object_name = 'publisher'
    template_name = 'books/my_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context


class MachineBookList(ListView):
    queryset = Book.objects.filter(publisher__name='机械工业出版社')
    context_object_name = 'book_list'
    template_name = 'books/machine_list.html'


class PublisherBookList(ListView):
    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publisher'] = self.publisher
        return context


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj


class AuthorCreate(CreateView):
    model = Author
    fields = ['salutation', 'name', 'email', 'headshot']
    template_name = 'books/author_create.html'
    context_object_name = 'form'

    def form_valid(self, form):
        print('新用户注册了')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('输入不合法')
        return super().form_invalid(form)


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['salutation', 'name', 'email', 'headshot']
    template_name = 'books/author_update.html'
    context_object_name = 'author'


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('books:publisher_list')
    template_name = 'books/author_delete.html'
    context_object_name = 'author'



