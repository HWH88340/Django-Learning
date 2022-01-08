from django import forms

class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all':('main.css',)
        }
        js = ('https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.js', )

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100, help_text='你的大名',widget=forms.Textarea(
        attrs={'style':'color:red','class': 'special'}))
    age = forms.IntegerField(label='Your age', error_messages={
        'required':'xxxx',
        'max_value':'xxxx'
    })
    email = forms.EmailField(disabled=True)
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    birth_year = forms.DateField()
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
    date = forms.DateField(widget=CalendarWidget)




class ContactForm(forms.Form):
    subject = forms.CharField(label='邮件主题', max_length=100,min_length=2)
    message = forms.CharField(widget=forms.Textarea,error_messages={'required': 'Please enter your messgae'})
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)



    field_order = ['message', 'subject']

    # def clean(self):
    #     #pass 做你自己的验证工作
    #     return super().clean()



from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        # fields = ['name', 'title', 'birth_date']
        fields = '__all__'
        # exclude = ['name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']