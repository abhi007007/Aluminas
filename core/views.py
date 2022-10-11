from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    print(request.user)
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    return render(request,'index.html')
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        print(email), print(password)
        if email  == "" or password =="":
            messages.info(request, "please fill all the fields")
            return redirect('login')
        else:
            user = auth.authenticate(username=email, password=password)
            
            print(user)
            if user is not None:
                auth.login(request, user)
                print(request.user)
                return redirect('home')
            else:
                messages.info(request, 'Invalid Credentials')
                return render(request, 'login.html')

    else:
        return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['pass1']
        if pass1 == "" or pass2 == ""or email == "":
            messages.info(request, 'please fill all the fields')
            return redirect('register')
        else:
            if pass1 == pass2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return redirect('register')
                else:

                    user = User.objects.create_user(
                        username=email, password=pass1, email=email)
                    user.save()
                    usern = auth.authenticate(username=email, password=pass1)
                    auth.login(request, usern)
                    return redirect('home')
            else:
                messages.info(request, 'Password not matching')
                return redirect('register')

    else:
        return render(request, 'registration.html')        

def home(request):
    return render(request,'home.html')