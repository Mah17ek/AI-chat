from .models import Home_page
from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
import smtplib
import email.message
from smtplib import SMTP 

import random

def Index(request):
    return HttpResponse('<h1> hello </h1>')

def login_pag(request):
    if request.method == "POST":
        try:
            m = Home_page.objects.get(useremail = request.POST['useremail'])
            if m.password == request.POST['password']:
                print(m.useremail)
                request.session['email'] = m.useremail
                return redirect('index')
            else:
                return HttpResponse("<h2><a href=''>You have entered wrong password</a></h2>")
        except:
            return HttpResponse("<h2><a href=''>no username found.</a></h2>")
    return render(request,'login.html')
   

def create_account(request):
    if request.POST:
         fname   =request.POST['fname']
         lname  = request.POST['lname']
         Email  = request.POST['Email']
         ph      = request.POST['ph']   
         password  = request.POST['password']
         cpassword   = request.POST['cpassword']
        
    
         print(fname,lname,Email,ph,password,cpassword)
    
         obj = Home_page()
         obj.fname =  fname     
         obj.lname =  lname     
         obj.useremail = Email 
         obj.phone = ph     
         obj.password =  password  
         obj.cpassword  = cpassword 
         obj.save() 
    return render(request,'create.html')

def Forget_password(request):
    if request.POST:
        email1 = request.POST['email']
        number1 = request.POST['phn']
            
        try:
            valid = Home_page.objects.get(useremail=email1)
            if int(valid.phone) == int(number1):
                print(email1)
                request.session['useremail'] = email1
                
                numbers = [1,2,3,4,5,6,7,8,9,0]
                num = ""
                for i in range(4):
                    num += str(random.choice(numbers))
                
                num = int(num)
                print(num)
                
                # ============== Email ==============
                
                sender_email = "devarshmistry25@gmail.com"  
                sender_pass = "dev@rsh26"
                receiver_email = email1

                server = smtplib.SMTP('smtp.gmail.com',587)

                your_message =  "This Is Your OTP Number = "+str(num)

                print(your_message)

                msg = email.message.Message()
                msg['Subject'] = "Your OTP From Advance Billing System"
                msg['From'] = sender_email
                msg['To'] = receiver_email
                password = sender_pass
                msg.add_header('Content-Type','text/html')
                msg.set_payload(your_message)

                server.starttls()
                server.login(msg['From'],password)
                server.sendmail(msg['From'],msg['To'],msg.as_string())
                
                # ============== End Email ===========
                
                request.session['otp'] = num
                
                return render(request,'otp.html',{'otp':num})
                                    
            else:
                return HttpResponse("<h2><a href=''>Mobile Number Is Not Registered</a></h2>")
                return redirect('forgotpass')
        except:
            return HttpResponse("<h2><a href=''>Email Is Not Registered</a></h2>")
            return redirect('forgotpass')
        
    return render(request,'forget.html')

def otp(request):
    if request.session.has_key('otp'):
        if request.POST:
            otp = request.POST['otp']
            if int(request.session['otp']) == int(otp):
                del request.session['otp']
                return redirect('newpassword')
            else:
                return HttpResponse("<h2><a href=""> You Have Entered Wrong OTP </a></h2>")
        else:
            return redirect('forgotpass')
    return redirect('login')
    
def password(request):
    if request.session.has_key('useremail'):
        if request.POST:
            pass_1 = request.POST['pass1']
            pass_2 = request.POST['pass2']
            
            if pass_1 == pass_2:
                valid = Home_page.objects.get(useremail=request.session['useremail'])
                valid.password = pass_2
                valid.save()
                del request.session['useremail']
                return redirect('login')
            else:
                return HttpResponse("<h2><a href=''>Passwords Are Not Same ...</a></h2>")
        return render(request,'New_Pass.html')
    return redirect('login')
    return render(request,'newpass.html')
     
def bot(request):
    return render(request,'bot.html')

def logout(request):
    if 'User' in request.session.keys():
        del request.session['User']
        return redirect('login')
    else:
        return redirect('login')



