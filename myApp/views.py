from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#curd oparations
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from myApp.forms import *
from myApp.models import *
from datetime import date
from reportlab.pdfgen import canvas
from django.http import FileResponse

# Create your views here.

'''
def Home(request):
    return render(request, 'index.html')
def About(request):
    return render(request,  'about.html')


def Register(request):
  if request.method=='POST':
      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password') 
      
      if User.objects.filter(username = username).exists():
        messages.error(request, 'user username already exists')
        return redirect('login')
      
      if User.objects.filter(email = email).exists():
        messages.error(request, 'user email already exists')
        return redirect('login')
      
      if User.objects.filter(password = password).exists():
        messages.error(request, 'user password already exists')
        return redirect('login')
      
      user = User.objects.create_user(username = username, email = email, password = password)
      user.set_password(password)
      user.save()
      
      return redirect('login')
    
  return render(request, 'register.html')



def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(username, password)
        user = authenticate(request, username=username, password=password)

        print(user)
        if user is not None:
            login(request,user)
            #messages.success(request, 'Login successful. Welcome back!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Login failed. Please check your credentials.')
        return redirect('login')
            
    return render(request, 'login.html')


def Airlines(request):
 
    return render(request, 'airlines.html')
   
def Amazon_Web_Services(request):
 
    return render(request, 'amazon-web-services.html')

def Atlassian(request):
 
    return render(request, 'atlassian.html')
def Azure(request):
 
    return render(request, 'azure.html')

def Banking(request):
 
    return render(request, 'banking.html')

def Capital_Market(request):
 
    return render(request, 'capital-market.html')

def Careers(request):
 
    return render(request, 'career.html')

def Communications(request):
 
    return render(request, 'communications.html')

def Contact(request):
 
    return render(request, 'contact.html')

def Devops(request):
 
    return render(request, 'devops.html')

def Dynamic_Three(request):
 
    return render(request, 'dynamic-three.html')

def Energy_And_Utilities(request):
 
    return render(request, 'Energy-And-Utilities.html')

def Financial_Services(request):
 
    return render(request, 'financial-services.html')


def Healthcare_Life_Sciences(request):
 
    return render(request, 'healthcare-life-sciences.html')

def Healthcare(request):
 
    return render(request, 'healthcare.html')



def Insurance(request):
 
    return render(request, 'insurance.html')

def It_Consulting(request):
 
    return render(request, 'it-consulting.html')

def It_Outsource(request):
 
    return render(request, 'it-outsource.html')



def Logistics(request):
 
    return render(request, 'logistics.html')

def Manufacturing(request):
 
    return render(request, 'manufacturing.html')

def Media_Entertainment(request):
 
    return render(request, 'media-&-entertainment.html')

def Power_Apps(request):
 
    return render(request, 'power-apps.html')

def Product_Engineer(request):
 
    return render(request, 'product-engineer.html')

def Recruitments(request):
 
    return render(request, 'recruitments.html')

def Retail_Ecommerce(request):
 
    return render(request, 'retail-and-ecommerce.html')


def Retail(request):
 
    return render(request, 'retail.html')


def Sap_Consulting(request):
 
    return render(request, 'sap-consulting.html')


def Servicenow(request):
 
    return render(request, 'servicenow.html')


def Telecom(request):
 
    return render(request, 'telecom.html')

def Travel_Hospitality(request):
    
    return render(request, 'travel-&-hospitality.html')

def Travel(request):
    
    return render(request, 'travel.html')

def Work_Day(request):
    
    return render(request, 'work-day.html')

def Create_User(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(request.POST)  
        if form.is_valid():
            
            job_title = form.cleaned_data['job_title']
            date = form.cleaned_data['date']
            experience = form.cleaned_data['experience']
            qualification = form.cleaned_data['qualification']
            
            user_data = Career( job_title=job_title, date=date, experience=experience, qualification=qualification)
            user_data.save()
            print(user_data)
            
            return redirect('show_user_data') 
    else:
        form = UserForm()

    return render(request, 'user_list.html', {'form': form})

class Show_User_Data(ListView):
    model = Career
    template_name= 'show_user_detail.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        fm=UserForm()
        user_data = Career.objects.all()
        context={'user_data':user_data,'fm':fm,}
        
        return context
    def create_user(request):
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()  # This will save the form data to the User model
                return redirect('show_user_data')
        else:
            form = UserForm()
        
            
        return render(request,"show_user_detail.html")
    

class Update_User(UpdateView):
      model = Career
      fields = ('job_title', 'date', 'experience','qualification')
      template_name= 'user_form.html'
      success_url = reverse_lazy('show_user_data')

class Delete_User(DeleteView):
      model = Career
      template_name= 'user_confirm_delete.html'
      success_url = reverse_lazy('show_user_data')

def Applicants(requests):
    return render(requests, 'applicants.html')

def User_Detail(request, user_id):
    user = get_object_or_404(Career, id=user_id)
    return render(request, 'user_detail.html', {'user': user})
@login_required
def Dashboard(request):
    job_form_data = Job_Application.objects.all()
    return render(request, 'dashboard.html',locals())

#blog views
def Blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', locals())

def Create_Blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            image = form.cleaned_data['image']
            print(request.method)
            # Create a new Blog object and save it
            new_blog = Blog(title=title, content=content, image=image)
            new_blog.save()
            
            return redirect('show_blog_data')
    else:
        form = BlogForm()  # Use BlogForm instead of UserForm

    return render(request, 'blog_list.html', {'form': form})

class Show_Blog_Data(ListView):
    model = Blog
    template_name = 'show_blog_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = BlogForm()
        blog_data = Blog.objects.all()
        context['blog_data'] = blog_data
        context['fm'] = fm
        
        return context

    def create_blog(request):
        if request.method == 'POST':
            form = BlogForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('show_blog_data')
        else:
            form = BlogForm()
    
        return render(request, "show_blog_detail.html", {'form': form})

class Update_Blog(UpdateView):
      model = Blog
      fields = ('title', 'content', 'image')
      template_name= 'update_blog_form.html'
      success_url = reverse_lazy('show_blog_data')

class Delete_Blog(DeleteView):
      model = Blog
      template_name= 'blog_delete.html'
      success_url = reverse_lazy('show_blog_data')

def Blog_Detail(request, user_id):
    blog = get_object_or_404(Blog, id=user_id)
    return render(request, 'blog_detail.html', {'blog': blog})

def Job_Career(request):
    career = Career.objects.all()
    return render(request, 'job_career.html', locals() )


def job_application(request):
    if request.method == 'POST':
        form = Job_Application_Form(request.POST)
        print(request.POST)  

        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            date = request.POST.get('date')
            phone_number = request.POST.get('phone_number')
            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            pdf_file = request.FILES.get('pdf_file')
            gender = request.FILES.get('gender')
           
   
            job_application_data = Job_Application(username=username, email=email, date=date, phone_number=phone_number, address1=address1,address2=address2, pdf_file = pdf_file ,gender=gender)
            
            job_application_data.save()
        
            return redirect('success_page')
    else:
        form = Job_Application_Form()

    return render(request, 'job_application.html', locals())

#this function pdf file how to download df

def generate_pdf(job_application):
    response = FileResponse(open('job_application.pdf', 'wb'))
    p = canvas.Canvas(response)
    # Write your model data to the PDF
    p.drawString(100, 750, "Job Application Details")
    p.drawString(100, 700, f"Username: {job_application.username}")
    # Add more fields as needed
    p.showPage()
    p.save()
    return response

def generate_pdf_view(request, id):
    job_application = get_object_or_404(Job_Application, id=id)
    return generate_pdf(job_application)'''


def Success_Page(request):
    return render(request, 'success_page.html')




#new views code 
from django.shortcuts import render, redirect
from .forms import GovtEventForm
from django.shortcuts import render, get_object_or_404, redirect


def event_list(request):
    events = GovtEvent.objects.all()
    return render(request, 'govt_event/event_list.html', {'events': events})


# views.py
from django.shortcuts import render, redirect
from .forms import GovtEventForm

def create_event(request):
    if request.method == 'POST':
        form = GovtEventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')
        else:
            print(form.errors)
    else:
        form = GovtEventForm()

    return render(request, 'govt_event/create_event.html', {'form': form})

def edit_event(request, event_id):
    event = get_object_or_404(GovtEvent, pk=event_id)
    
    if request.method == 'POST':
        form = GovtEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to the event list page
    else:
        form = GovtEventForm(instance=event)

    return render(request, 'govt_event/edit_event.html', {'form': form, 'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(GovtEvent, pk=event_id)
    event.delete()
    return redirect('event_list')  