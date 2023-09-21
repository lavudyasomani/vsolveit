from django import forms
from myApp.models import *
from django.contrib.auth.forms import AuthenticationForm
from .models import Job_Application

'''

class Job_Application_Form(forms.ModelForm):
    class Meta:
        model = Job_Application
        exclude = ['date']
        fields = ['username', 'email', 'phone_number', 'address1', 'address2', 'image']
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@gmail.com'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone number'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'date'}))
    address1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address1'}))
    address2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address2'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

'''


class Job_Application_Form(forms.Form):
    class Meta:
        model = Job_Application
        
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()  
    date = models.DateField(auto_now=True) 
    address1 = models.TextField(max_length=300)  
    address2 = models.TextField(max_length=300) 
    pdf_file = models.FileField(upload_to='pdfs/')
    gender = models.CharField(max_length=10)
    
class Login_Form(AuthenticationForm):
    
    username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

#user form
class UserForm(forms.Form):
    
    job_title = forms.CharField(max_length=100)
    date = forms.DateField()
    experience = forms.CharField(max_length=100)
    qualification = forms.CharField(max_length=100)
    
#blog form  
class BlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()

