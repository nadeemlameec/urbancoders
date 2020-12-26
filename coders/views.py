from django.shortcuts import render,get_object_or_404
from coders.models import Form
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"home.html")
def form(request):
    if request.method == "POST":
        Name=request.POST.get("Name")
        Last_Name=request.POST.get("Last_Name")
        Email_id=request.POST.get("Email_id")
        form1=Form(Name=Name,Last_Name=Last_Name,Email_id=Email_id)
        form1.save()
        messages.success(request, 'Your Detail has been Stored!')
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def graphic(request):
    return render(request,"graphic.html")


def digi(request):
    
    return render(request,"Digi.html")


def web(request):
    return render(request,"Web.html")    


def base(request):
    return render(request,"base.css")

