from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout 
from .models import*
from django.core.mail import send_mail
from random import randint
from django.conf import settings
from defmail import send_otp
import threading
def Homepage(request):
    return render(request,"app/home.html")
def Signuppage(request):
    return render(request,"app/register.html")
def contactpage(request):
    return render(request,"app/contact.html")
def blogpage(request):
    return render(request,"app/blog.html")
def RegisterUser(request):
    if request.POST['role']=="Candidate":
        role=request.POST['role']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        user=UserMaster.objects.filter(Email=email)
        if user:
            message= "User Already Exists"
            return render(request,"app/register.html",{"msg": message})
        else:
            if password==cpassword:
                otp=randint(100000,999999)
                newuser =UserMaster.objects.create(Role=role,Otp=otp,Email=email,Password=password)
                otp_code=newuser.Otp
                user_email=newuser.Email
                success, messages= send_otp(otp_code,user_email)
                if success:
                    print(messages)
                    # Proceed with your view logic (e.g., render a success page)
                    newcand = Candidate.objects.create(user_id=newuser,FirstName=fname,LastName=lname)
                    return render(request,"app/otpverify.html",{'email':email})
                else:
                    print(f"Failed to send: {messages}")
                    return render("Error")
                
    else:
        print("Company Registration")
        if request.POST['role']=="Company":
                role=request.POST['role']
                fname=request.POST['fname']
                lname=request.POST['lname']
                email=request.POST['email']
                password=request.POST['password']
                cpassword=request.POST['cpassword']
                user=UserMaster.objects.filter(Email=email)
                if user:
                    message= "User Already Exists"
                    return render(request,"app/companyreg.html",{"msg": message})
                else:
                    if password==cpassword:
                        otp=randint(100000,999999)
                        newuser =UserMaster.objects.create(Role=role,Otp=otp,Email=email,Password=password)
                        otp_code=newuser.Otp
                        user_email=newuser.Email
                        otp_code=newuser.Otp
                        success, messages= send_otp(otp_code,user_email)
                        email_thread = threading.Thread(
                                target=send_otp, 
                                args=(otp_code,user_email)
                            )
                        email_thread.start()
                        
                        if success:
                            print(messages)
                                            # Proceed with your view logic (e.g., render a success page)
                        else:
                            print(f"Failed to send: {messages}")
                        
                        newcompany = Company.objects.create(user_id=newuser,FirstName=fname,LastName=lname)
                        return render(request,"app/otpverify.html",{'email':email})
         
def Companyregister(request):
    return render(request,"app/company/index.html")

def OtpVerify(request):
    if request.method == "POST":
        email=request.POST.get('email')
        otp = request.POST.get('otp', '').strip()
        print(email)
        user = UserMaster.objects.filter(Email=email).first()
        
        if user:
            if str(user.Otp) == str(otp):
                message = "Otp verified Successfully"
                messages.success(request,message)
                return redirect("login")
            else:
                message = "Otp is incorrect"
                return render(request,"app/otpverify.html",{"msg":message})
        else:
            messages.error(request, "Account not found. Please register first.")
            return redirect("register")
    return render(request, "app/otpverify.html")
def loginpage(request):
    return render(request,"app/login.html")
def loginUser(request):
    if request.POST['role'] =="Candidate":
        email= request.POST['email']
        password= request.POST['password']
        user=UserMaster.objects.get(Email=email)
        if user:
           if user.Password==password and user.Role=="Candidate":
               can = Candidate.objects.get(user_id=user)
               request.session['id']=user.id
               request.session['role']=user.Role
               request.session['fname']=can.FirstName
               request.session['lname']=can.LastName
               request.session['email']=user.Email
               return redirect("home")
           else:
               message = "User or Password doesnot  match"
               return render(request,"app/login.html",{"msg":message})
        else:
            message= "User doesnot exist"
            return render(request,"app/login",{"msg":message})
    else:
       email= request.POST['email']
       password= request.POST['password']
       user=UserMaster.objects.get(Email=email)
       if user:
            if user.Password==password and user.Role=="Company":
                comp = Company.objects.get(user_id=user)
                request.session['id']=user.id
                request.session['role']=user.Role
                request.session['fname']=comp.FirstName
                request.session['lname']=comp.LastName
                request.session['email']=user.Email
                request.session['password']=user.Password
                return redirect("companyindex")
            else:
                message = "User id or Password doesnot  match"
                return render(request,"app/login.html",{"msg":message})
       else:
            try:
                message= "User doesnot exist"
                return render(request,"app/login",{"msg":message})
            except UserMaster.DoesNotExist:
                 messages.error(request, "Invalid Email, Password, or Role selection.")
                 return render(request,"app/login.html")
        
def Profilepage(request,pk):
 
    user=UserMaster.objects.get(pk=pk)
    can=Candidate.objects.get(user_id=user)
    return render(request,"app/profile.html",{"user":user,"can":can})  
def Profileupdate(request,pk):
      user=UserMaster.objects.get(pk=pk)
      if user.Role=="Candidate":
          
        can=Candidate.objects.get(user_id=user)
        can.Contact=request.POST['phone']
        can.State=request.POST['state']
        can.City=request.POST['city']
        can.Gender=request.POST['gender']
        can.job_type=request.POST['job_type']
        can.jobcategory=request.POST['job_category']
        can.highestedu=request.POST['education']    
        can.website=request.POST['website']
        can.country=request.POST['country'] #First country belong to DB and second is user entered html input
        can.Profile_pic=request.FILES['jd_file']
        can.min_salary=request.POST['min_salary']
        can.max_salary=request.POST['max_salary']
        can.jobdescription=request.POST['description']
        can.experience=request.POST['experience']
        can.save()
        url = f'/profile/{pk}'
        return redirect(url)
        
def Applypage(request,pk):
    user=request.session['id']
    if user:
        cand=Candidate.objects.get(user_id=user)
        job=JobDetails.objects.get(id=pk)
        
    return render(request,"app/apply.html",{"user":user,"cand":cand,"job":job}) 

def Applyjob(request,pk):
       user=request.session.get('id')
       if user :
            try:
                cand=Candidate.objects.get(user_id=user)
                job=JobDetails.objects.get(id=pk)
            except (JobDetails.DoesNotExist, Candidate.DoesNotExist):
                messages.error(request, "The job listing or candidate profile could not be found.")
                return redirect('joblist')
            already_applied = ApplyList.objects.filter(candidate=cand, job=job).exists()
            if request.method=="POST":
                if already_applied:
                    message = "You have already applied to this job."
                    return render(request, "app/apply.html", {"msg": message, "job": job, "error": True})
                ed = request.POST.get('education')
                exp = request.POST.get('experience')
                website = request.POST.get('website')
                gender = request.POST.get('gender')
                min_salary = request.POST.get('min_salary')
                max_salary = request.POST.get('max_salary')
                resume = request.FILES.get('resume')
                try:
                    newapply=ApplyList.objects.create(candidate=cand,job=job,education=ed,
                                                      experience=exp,website=website,gender=gender,
                                                      resume=resume,min_salary=min_salary,max_salary=max_salary)
                    already_applied = True                                                              
                    message="Applied Job Successfully"
                    return render(request,"app/apply.html",{"msg":message,"job": job,"already_applied": already_applied})                     
                except Exception as e:
                    print(f"❌ DATABASE SAVE CRASH REASON: {str(e)}")
                
            return render(request, "app/apply.html",{"job": job,"already_applied": already_applied})
       else:
            return redirect('login')
     
############################## Company Side ####################################################

def Companyindexpage(request):
    all_job=JobDetails.objects.all()
    return render(request,"app/company/index.html",{'all':all_job})

def Companyprofilepage(request,pk):
    user=UserMaster.objects.get(pk=pk)
    company=Company.objects.get(user_id=user)
    return render(request,"app/company/companyprofile.html",{'user':user,"comp":company})

def Companyprofileupdate(request,pk):
        user=UserMaster.objects.get(pk=pk)
        if user.Role=="Company":
            if request.method=="POST":
                comp=Company.objects.get(user_id=user)
                
                comp.CompanyName = request.POST.get('compname')
                comp.FirstName = request.POST.get('firstname')
                comp.LastName = request.POST.get('lastname')
                comp.Comp_Contact = request.POST.get('contact')
                comp.State = request.POST.get('state')
                comp.City = request.POST.get('city')
                comp.Comp_web = request.POST.get('website')
                comp.Logo_pic=request.FILES.get('logo_image')
                comp.Comp_description =request.POST.get('description')    
                comp.save() 
                url = f'/companyprofile/{pk}'
                return redirect(url)

def JobPostPage(request):
    return render(request,"app/company/jobpost.html")

def JobDetailsSubmit(request):
    try:
        user_id = request.session.get('id')
        user=UserMaster.objects.get(id=user_id)
    except (UserMaster.DoesNotExist, TypeError):
        messages.error(request, "Your session has expired or your user account was not found. Please log in again.")
        return redirect('login')
    if user.Role=='Company':
        comp=Company.objects.get(user_id=user)
        jobname=request.POST['jobname']
        companyname=request.POST.get('companyname')
        address=request.POST.get('companyaddress')
        companycontact=request.POST['contact']
        companyemail=request.POST['email']
        jobdescription=request.POST['description']
        qualification=request.POST['qualification']
        experience=request.POST['experience']
        responsibility=request.POST['responsibility']
        location=request.POST['location']
        salary=request.POST['salary']
        website=request.POST['website']
        logo=request.FILES['logo']
        
        newjob=JobDetails.objects.create(company_id=user,jobname=jobname,companyname=companyname,companyaddress=address,
                                         jobdescription=jobdescription,qualification=qualification,resposibilities=responsibility,
                                         location=location,companywebsite=website,salarypackage=salary,logo=logo,
                                         companyemail=companyemail,companycontact=companycontact,experience=experience)
        message="Job Post Successfully"
        return render(request,"app/company/jobpost.html",{"msg":message})

  
def tableshow(request):
    all_job=JobDetails.objects.all()
    return render(request,"app/company/tables.html",{"alljobs":all_job})

def candidatejoblist(request):
    all_job=JobDetails.objects.all()
    return render(request,"app/browse-jobs.html",{"alljobs":all_job})
def companylogout(request):
    request.session.flush() 
   
    
    return redirect("home")

def Jobapplylist(request):
    all_jobapply=ApplyList.objects.all()
    return render(request,"app/company/applyjoblist.html",{"all_job":all_jobapply})
def forgotpassword(request):
    return render(request,"app/company/password.html")

######################################### ADMIN SIDE  ##############################################
def AdminLoginPage(request):
    return render(request,"app/Admin/login.html")
def Adminindex(request):
    
    if 'username' in request.session and 'password' in request.session:
             return render(request,"app/Admin/index.html",)
    else:
        return redirect("adminpage")
def AdminLogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if username=="admin" and password=="admin":
            request.session['username']=username
            request.session['password']=password
            return redirect("adminindex")
        else:
            message="Username or password not Matched"
            return render(request,"app/Admin/login.html",{"msg":message})
           
def Adminuserlist(request):
    all_user=UserMaster.objects.filter(Role="Candidate")
    return render(request,"app/Admin/userlist.html",{"alluser":all_user})

def Admincompanylist(request):
    all_company=UserMaster.objects.filter(Role="Company")
    return render(request,"app/Admin/companyuserlist.html",{"allcompany":all_company})


def userdelete(request,pk):
    user=UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('userlist')

def verifycompany(request,pk):
    company=UserMaster.objects.get(pk=pk)
    if company:
        return render(request,"app/Admin/verify.html",{"company":company})
    
def verifypage(request,pk):
    company=UserMaster.objects.get(pk=pk)
    if company:
        company.Is_verfied=request.POST['verify']
        company.save()
        return redirect('companylist')
def companydelete(request,pk):
    company=UserMaster.objects.get(pk=pk)
    company.delete()
    return redirect('companylist')
