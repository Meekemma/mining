from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email Address'}),
            'body': forms.Textarea(attrs={'placeholder':'Comment'}),
        }

        error_messages ={
           'name': {
                'required': 'Please enter your name.',
                'max_length': 'The name cannot exceed 20 characters.',
            },

            'email': {
                'required': 'Please enter your email address.',
                'invalid': 'Please enter a valid email address.',
            },

            'body': {
                'required': ' Please enter your text '
            }
        }

        labels={
            'body':'Message'
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=[ 'username','first_name', 'last_name', 'email', 'password1', 'password2']


        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter  Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email Address'}),
            'password1': forms.PasswordInput(render_value=True,attrs={'placeholder': 'Enter Password'}),
            'password2': forms.PasswordInput(render_value=True,attrs={'placeholder': 'Re-enter Password'}),
        }

        


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'        
        exclude=['user']

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter  Username'}),
            'gender': forms.Select(attrs={'placeholder': 'Gender'}),
            'birth_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Mobile Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email Address'}),
            'country': forms.Select(attrs={'placeholder': 'Select Country'}),
            'state': forms.TextInput(attrs={'placeholder': 'Enter State'}),
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'gender': 'Gender',
            'birth_date': 'Birth Date',
            'phone': 'Phone Number',
            'email': 'Email Address',
            'country': 'Country',
            'state': 'State',
        }



class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['deposit_amount']  # Add 'profile' field to the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
         # Add CSS class to the profile field
        self.fields['deposit_amount'].widget.attrs.update({'class': 'form-control'}) 
        
         # Add CSS class to the deposit_amount field
class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = ['withdrawal_amount']  # Add 'profile' field to the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
         # Add CSS class to the profile field
        self.fields['withdrawal_amount'].widget.attrs.update({'class': 'form-control'}) 