from django import forms
from myApp.models import *
from django.contrib.auth.forms import AuthenticationForm
from myApp.models import *



# forms.py
from django import forms
from .models import GovtEvent

class GovtEventForm(forms.ModelForm):
    class Meta:
        model = GovtEvent
        exclude = []  # Exclude all fields, as we are using widgets directly
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'parliament': forms.Select(attrs={'class': 'form-control'}),
            'assembly': forms.Select(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Venue'}),
            'pre_event_image': forms.FileInput(attrs={'class': 'form-control'}),
            'mid_event_image': forms.FileInput(attrs={'class': 'form-control'}),
            'post_event_image': forms.FileInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }





'''class GovtEventForm(forms.ModelForm):
    class Meta:
        model = GovtEvent
        fields = '__all__' 
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'parliament': forms.Select(attrs={'class': 'form-control'}),
            'assembly': forms.Select(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Venue'}),
            'pre_event_image': forms.FileInput(attrs={'class': 'form-control'}),
            'mid_event_image': forms.FileInput(attrs={'class': 'form-control'}),
            'post_event_image': forms.FileInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
'''

'''class GovtEvent_Form(forms.Form):
    class Meta:
        model = GovtEvent
        
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()  
    date = models.DateField(auto_now=True) 
    address1 = models.TextField(max_length=300)  
    address2 = models.TextField(max_length=300) 
    pdf_file = models.FileField(upload_to='pdfs/')
    gender = models.CharField(max_length=10)'''
    
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

