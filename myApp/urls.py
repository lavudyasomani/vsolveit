from django.urls import path
from myApp.views import *
from django.contrib.admin.views.decorators import staff_member_required


# urls.py
from django.urls import path
from .views import event_list, create_event, edit_event, delete_event

urlpatterns = [
    
   
    path('events/', event_list, name='event_list'),
    path('', create_event, name='create_event'),
    path('events/<int:event_id>/edit/', edit_event, name='edit_event'),
    path('events/<int:event_id>/delete/', delete_event, name='delete_event'),
]













'''urlpatterns = [
   
    path('', Home, name='home'),
    path('login/', user_login, name='login'),
    path('register/', Register, name='register'),
    ##path('register/', register_view, name='register'),
    path('about/', About, name='about'),
    path('airlines/', Airlines, name='airlines'),
    path('aws/', Amazon_Web_Services, name='aws'),
    path('atlassian/', Atlassian, name='atlassian'),
    path('azure/', Azure, name='azure'),
    path('banking/', Banking, name='banking'),
    path('capital_market/', Capital_Market, name='capital_market'),
    path('career/', Careers, name='career'),
    path('communications/', Communications, name='Communications'),
    path('contact/', Contact, name='contact'),
    path('devops/', Devops, name='devops'),
    path('dynamic_three/', Dynamic_Three, name='dynamic_three'),
    path('eu/', Energy_And_Utilities, name='eu'),
    path('fs/', Financial_Services, name='fs'),
    path('hls/', Healthcare_Life_Sciences, name='hls'),
    path('healthcare/', Healthcare, name='healthcare'),
    path('insurance/', Insurance, name='insurance'),
    path('It_Consulting/', It_Consulting, name='It_Consulting'),
    
    path('It_Outsource/', It_Outsource, name='It_Outsource'),
    path('logistics/', Logistics, name='logistics'),
    path('manufacturing/', Manufacturing, name='manufacturing'),
    path('me/', Media_Entertainment, name='me'),
    path('power_apps/', Power_Apps, name='power_apps'),
    path('pe/', Product_Engineer, name='pe'),
    path('recruitments/', Recruitments, name='recruitments'),
    path('retail_ecommerce/', Retail_Ecommerce, name='retail_ecommerce'),
    
    path('retail/', Retail, name='retail'),
    path('sap_consulting/', Sap_Consulting, name='sap_consulting'),
    path('servicenow/', Servicenow, name='servicenow'),
    path('telecom/', Telecom, name='telecom'),
    path('th/', Travel_Hospitality, name='th'),
    path('travel/', Travel, name='travel'),
    path('work_day/', Work_Day, name='work_day'),
    
    
    #curd oparations urls
    path('create_user/', Create_User, name='create_user'),
    #path('',Create_User.as_view(), name="create_user"),
    path("show_user_data/", Show_User_Data.as_view(), name='show_user_data'),
    path('update_user/<int:pk>/', Update_User.as_view(), name="update_user"),
    path('delete_user/<int:pk>/',Delete_User.as_view(), name="delete_user"),
    path('Applicants', Applicants, name='Applicants'),
   
    path('user/<int:user_id>/', User_Detail, name='user_detail'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('job_career/', Job_Career, name='job_career'),
    path('jpb_application/', job_application, name='job_application'),
    path('success_page/',Success_Page, name='success_page'),
    path('generate_pdf/<int:id>/', generate_pdf_view, name='generate_pdf'),


    
    #blog urls
    path('blog/', Blogs , name='blog'),
    path('create_blog/', Create_Blog, name='create_blog'),
    path('show_blog_data/', Show_Blog_Data.as_view() , name='show_blog_data'),
    path('update_blog/<int:pk>/', Update_Blog.as_view(), name='update_blog'),
    path('delete_blog/<int:pk>/', Delete_Blog.as_view(), name='delete_blog'),
    path('blog_detail/<int:user_id>/', Blog_Detail, name='blog_detail')
    
]
     '''