import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

if __name__ == '__main__':
    import django
    django.setup()
    from app.models import Author
    print(Author.objects.values())