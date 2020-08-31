from django.shortcuts import render, redirect
from django.http import HttpResponse

from evmanage.models import Event,student
from django.contrib import messages
from django.contrib.auth.models import User, auth



def index(request):
    return render(request, "index.html")




def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('details')
        else:
            messages.info(request, 'INVALID USERNAME /PASSWORD')
            return redirect('index')
    else:
        return render(request,'index')

def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('index')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('index')
            else:    
                user =  User.objects.create_user(first_name=first_name, last_name=last_name,  email=email, username=username, password=password1)
                user.save();
                messages.info(request,'user created pls login')
                return redirect('index')

        else:
            
            return redirect('index')
        return redirect('/')

        

    else:
        return render(request,'signup.html')



def logout(request):
    auth.logout(request)
    return redirect('/')


def details(request):
    if request.method=="POST":
        cult = request.POST.get('cultural')
        tech = request.POST.get('technical')
        if cult or tech:
            listsc = Event.objects.filter(E_type="cultural")
            listst = Event.objects.filter(E_type="technical")
            if cult:
                lists=listsc
                return render(request,'event.html', {'lists':lists})
            else:
                lists=listst
                return render(request,'event.html', {'lists':lists})
        else:
            return redirect('details')
    return render(request,"details.html")



def register(request):
    if request.method == 'POST':
        USN = request.POST['USN']
        name = request.POST['name']
        branch = request.POST['branch']
        sem = request.POST['sem']
        college = request.POST['college']
        email = request.POST['email']
        contact = request.POST['contact']
        payment_mode = request.POST.get('payment_mode')
        account_no = request.POST['account_no'] 
        cvv = request.POST['cvv'] 
        exp_date = request.POST['exp_date'] 
        E_id_id = request.POST['E_id_id']
        
        user1 =  student.objects.create(USN=USN, name=name,  branch=branch, sem= sem, college=college, email=email, E_id_id=E_id_id ,contact=contact, payment_mode=payment_mode , account_no =account_no,cvv = cvv,exp_date = exp_date)
        user1.save();
        return redirect('registered')

    else:
        return render(request, 'register.html')


def registered(request):
    return render(request, 'registered.html')

def event(request):
    return render(request, 'event.html')