from django import forms


class Login(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, required=True,
                           widget=forms.TextInput(attrs={'class': 'form_item','placeholder': 'Имя'}))
    password = forms.CharField(label='Пароль', max_length=100, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form_item','placeholder': '*******'}))

class Registration(Login):
    name = forms.CharField(label='Имя', max_length=100, required=True,
                           widget=forms.TextInput(attrs={'class': 'form_item','placeholder': 'Имя'}))
    email = forms.EmailField(label='Почта', max_length=100, required=True,
                             widget=forms.EmailInput(attrs={'class': 'form_item','placeholder': 'SemGusb@yandex.ru'}))
    password = forms.CharField(label='Пароль', max_length=100, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form_item','placeholder': '*******'}))