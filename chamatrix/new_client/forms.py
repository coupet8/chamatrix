from django import forms
BIRTH_YEAR_CHOICES = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959',
'1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969',
'1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979',
'1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
'1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999',
'2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009']
YEAR_CHOICES = [('1', '2023')]
 
class UserForm(forms.Form):
    first_name = forms.CharField(label="Имя", min_length=2, max_length=30)
    last_name = forms.CharField(label="Фамилия", min_length=2, max_length=30)
    email = forms.EmailField(label="Email", required=False, min_length=7, max_length=255)
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES), label="Дата рождения")
    year = forms.ChoiceField(widget=forms.RadioSelect, choices=YEAR_CHOICES, label="Прогнозный год")
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-group'})
