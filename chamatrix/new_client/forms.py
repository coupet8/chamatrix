from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class MyDateInput(forms.DateInput):
    input_type = 'date'
    format = '%d.%m.%Y'

YEAR_CHOICES = [('1', '2023')]
 
class UserForm(forms.Form):
    first_name = forms.CharField(label="Имя", min_length=2, max_length=30)
    last_name = forms.CharField(label="Фамилия", min_length=2, max_length=30)
    #email = forms.EmailField(label="Email", required=False, min_length=7, max_length=255)
    birthday = forms.DateField(label='Дата рождения', required=True, widget=MyDateInput({'class': 'form-control'}))
    year = forms.ChoiceField(choices=YEAR_CHOICES, label="Прогнозный год")
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-group'})
