from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import *
from Minor import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate,login,logout
from .models import QuestionsFor10th


# My user and Super user
# superUser :-
# username --> nirajchittodiya
# password --> samp

# Create your views here.
def tenth(request):
    q_list = QuestionsFor10th.objects.all()
    length = len(q_list)
    ans_count = 0
    user_ans = []
    if request.method == 'POST':
        for qst in q_list:
            user_ans.append(request.POST.get(qst.Q_name))

        print(user_ans)

        # q_ans = request.POST.get('all_ans')
        # q_ans = q_ans.split()
        i=0
        for question in q_list:
            correct_ans = question.correct_ans
            if user_ans[i] == correct_ans:
                ans_count += 1
            print(correct_ans," ",user_ans[i])
            i+=1
        # i=0
        # for qst in q_list:
        #     if[user_ans[i] == qst.correct_ans]:
        #         ans_count += 1
        #         print(ans_count)
        #     print(user_ans[i]," ",qst.correct_ans)
        #     i+=1
        #     if i>length:
        #         break

        print(ans_count)
        grade = (ans_count*100)//length
        print(grade)
        if grade<35:
            return render(request,'arts.html')
        elif grade>35 and grade<=60:
            return render(request,'commerce.html')
        elif grade>60 and grade<=90:
            return render(request,'science.html')
        elif grade>90:
            return render(request,'topper.html')
        # return redirect('Test')


    return render(request,'10th.html',
    {'question_list':q_list,'length':length})


def home(request):
    return render(request,'minor1.html')

def Test(request):
    return render(request,'test.html')

def Userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST['pass2']

        user = authenticate(request,password=password,username=username)

        if user is not None:
            login(request,user)
            # fname = user.fname
            return render(request,'afterLogin.html',{'username':username})
            # return base(request,fname)
        else:
            messages.error(request,'Bad credentials')
            redirect('/login')
    return render(request,'minor_login.html')

def register(request):
    if request.method == "POST":
        fname = request.POST.get('firstName')
        lname = request.POST.get('lastName')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # applying filters 
        if User.objects.filter(username=username):
            messages.error(request,"Username is already exists!/n Try another username")
            return redirect('register')
        
        if User.objects.filter(email=email):
            messages.error(request,'Email is already exists')
            return redirect('register')

        if len(username)>10:
            messages.error(request,'Username must be under 10 characters')
            return redirect("register")

        if pass1!=pass2:
            messages.error(request,"Your password isn't matching")
            return redirect('register')

        if not username.isalnum():
            messages.error(request,"Username must be alpha neumeric")
            return redirect('register')

        my_user = User.objects.create_user(username,email,pass2)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.is_active = True
        my_user.save()

        messages.success(request,'Your account is succesfully created & we send you a mail regarding it')

        # welcome email
        subject = "Welcome to web based career guidance system"

        msg = "Hello "+ my_user.first_name + "!!\n"+"Welcome to our web base career guidnace system \n"+"We sent you a confirmation link in order to activate your account\n\n"+'Thanks and regards Niraj Chittodiya'
        from_email = settings.EMAIL_HOST_USER
        list_to = [my_user.email]
        send_mail(subject,msg,from_email,list_to,fail_silently=True)

        # Email address confirmation email
        current_site = get_current_site(request)
        email_subject = "Confirm your email @ mine"
        # msg2 = render_to_string('email-confirmtaion.html',{
        #     'name':my_user.first_name,
        #     'domain':current_site.domain,
        #     'uid':urlsafe_b64encode(force_bytes(my_user.pk))
        # })
        
        return redirect('login')

    return render(request,'minor_register.html')

def Userlogout(request):
    logout(request)
    return render(request,'minor1.html')

def twelth(request):
    pass

def Homeal(request):
    return render(request,'afterLogin.html')