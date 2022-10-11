from django.shortcuts import render

# Create your views here.
def index(request):
    print(request.user)
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    return render(request,'index.html')