from . import views
from django.urls import path,include
import os
from django.conf.urls.static import static 
from django.conf import settings
urlpatterns = [
   path("",views.Homepage,name="home"),
   path("signup/",views.Signuppage,name="signup"),
   path("register/",views.RegisterUser,name="register"),
   path("contact/",views.contactpage,name="contact"),
   path("blog/",views.blogpage,name="blog"),
   path("companyreg/",views.Companyregister,name="companyreg"),
   path("otp/",views.OtpVerify,name="otpverify"),
   path("login/",views.loginpage,name="login"),
   path("loginuser/",views.loginUser,name="loginuser"),
   path("profile/<int:pk>",views.Profilepage,name="profile") ,
   path("updateprofile/<int:pk>",views.Profileupdate,name="updateprofile"),
   path("joblist",views.candidatejoblist,name="joblist"),
   path("apply/<int:pk> ",views.Applypage,name="apply"),
   path("applyjob/<int:pk>/",views.Applyjob,name="applyjob"),
   
   ################################### Company Side #########################################
   path("companyindex",views.Companyindexpage,name="companyindex"),
   path("companyprofile/<int:pk>",views.Companyprofilepage,name="companyprofile"),
   path("companyprofileupdate/<int:pk>",views.Companyprofileupdate,name="companyprofileupdate"),
   path("jobpostpage/",views.JobPostPage,name="jobpostpage"),
   path("jobpost/",views.JobDetailsSubmit,name="jobpost"),
   path("tableshow/",views.tableshow,name="tableshow"),
   path("companylogout/",views.companylogout,name="companylogout"),
   path("applyjoblist/",views.Jobapplylist,name="applyjoblist"),
   path("forgotpassword/",views.forgotpassword,name="forgotpassword"),
   
   ######################################   Admin Side  #########################
   path("adminpage/",views.AdminLoginPage,name="adminpage"),
   path("adminlogin/",views.AdminLogin,name="adminlogin"),
   path("adminindex/",views.Adminindex,name="adminindex"),
   path("adminuserlist/",views.Adminuserlist,name="userlist"),
   path("companylist/",views.Admincompanylist,name="companylist"),
   path("deleteuser/<int:pk>",views.userdelete,name="deleteuser"),
   path("verifycompany/<int:pk>",views.verifycompany,name="verifycompany"),
   path("verifypage/<int:pk>",views.verifypage,name="verifypage"),
   path("companydelete/<int:pk>",views.companydelete,name="companydelete")
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)