from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginView(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request,username = username, password = password)
            if user is not None:
                login(request, user)
                return render(request,"portal/home.html")
            else:
                return redirect("loginView")
    else:
        return redirect("index")
    return render(request, "portal/login.html")

@login_required(login_url='loginView')
def logoutView(request):
    logout(request)
    return redirect("loginView")

@login_required(login_url='loginView')
def index(request):
    return render(request, "portal/home.html")

@login_required(login_url='loginView')
def examinationsView(request):
    return render(request, "portal/examinations.html")

@login_required(login_url='loginView')
def feesView(request):
    return render(request, "portal/fees.html")

@login_required(login_url='loginView')
def clearanceView(request):
    return render(request, "portal/clearance.html")

@login_required(login_url='loginView')
def newsView(request):
    return render(request, "portal/news.html")

@login_required(login_url='loginView')
def reportingView(request):
    return render(request, "portal/reporting.html")

@login_required(login_url='loginView')
def unitsView(request):
    return render(request, "portal/units.html")

@login_required(login_url='loginView')
def hostelView(request):
    return render(request, "portal/hostel.html")

@login_required(login_url='loginView')
def messagesView(request):
    return render(request, "portal/messages.html")

@login_required(login_url='loginView')
def profileView(request):
    return render(request, "portal/profile.html")