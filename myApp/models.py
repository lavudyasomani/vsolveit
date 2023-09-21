from django.db import models

#add users
class Career(models.Model):
    
    job_title = models.CharField(max_length=100, null=True)
    date = models.DateField()
    experience = models.CharField(max_length=100, null=True)
    qualification = models.CharField(max_length=100, null=True)
    
    
    def __str__(self):
            return self.job_title
#add blogs
class Blog(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to="img/")
    
    def __str__(self):
            return self.title
        

class Job_Application(models.Model):
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone_number = models.IntegerField(null=True)  
    date = models.DateField(auto_now=True, null=True) 
    address1 = models.TextField(max_length=300, null=True)  
    address2 = models.TextField(max_length=300, null=True) 
    pdf_file = models.FileField(upload_to='pdfs/')
    gender = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.username)

        
    