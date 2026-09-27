from django.db import models

class UserMaster(models.Model):
    Email = models.EmailField( max_length=50)
    Password = models.CharField(max_length=50)
    Otp = models.IntegerField(  )
    Role = models.CharField(max_length=50)
    Is_active = models.BooleanField(default=False)
    Is_verfied = models.BooleanField(default=False)
    Is_created = models.DateTimeField(auto_now_add=True)
    Is_updated = models.DateTimeField(auto_now_add=True)
    
class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Contact = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Address = models.CharField(max_length=150)
    Gender = models.CharField(max_length=50)
    Dob = models.CharField(max_length=50)
    min_salary = models.BigIntegerField()
    max_salary = models.BigIntegerField()
    job_type=models.CharField(max_length=150)
    jobcategory=models.CharField(max_length=150)
    country=models.CharField(max_length=50)
    highestedu=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    website=models.CharField(max_length=50)
    shift=models.CharField(max_length=50)
    jobdescription=models.CharField(max_length=50)
    Profile_pic = models.ImageField(upload_to="img/candidate")

class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    CompanyName = models.CharField(max_length=150)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Comp_Contact = models.CharField(max_length=50)
    Comp_Address = models.CharField(max_length=150)
    Comp_web=models.CharField(max_length=50)
    Comp_description=models.CharField(max_length=150)
    Logo_pic = models.ImageField(upload_to="app/img/company")
    
class JobDetails(models.Model):
    company_id=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    jobname =models.CharField(max_length=50)
    companyname=models.CharField(max_length=50)
    companyaddress=models.CharField(max_length=250)
    jobdescription=models.TextField(max_length=500)
    qualification=models.CharField(max_length=50)
    resposibilities=models.CharField(max_length=250)
    location=models.CharField(max_length=50)
    companywebsite=models.CharField( max_length=50)
    companyemail=models.CharField(max_length=250)
    companycontact=models.CharField(max_length=20)
    salarypackage=models.CharField(max_length=250)
    experience=models.IntegerField()
    logo = models.ImageField(upload_to="app/img/jobpost",default="")

class ApplyList(models.Model):
    candidate=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    job=models.ForeignKey(JobDetails,on_delete=models.CASCADE)
    education=models.CharField(max_length=50)
    experience=models.IntegerField(default=0)
    website=models.CharField(max_length=200)
    min_salary = models.CharField(max_length=200)
    max_salary = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    resume=models.FileField(upload_to="app/resume")
    
    
    
    
    
    