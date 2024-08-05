from django.shortcuts import render,redirect
from .models import siteuser

# Create your views here.
def home(request):
    if request.session.get("U") is not None:
        return redirect("http://localhost:8000/home/")
    Username=request.POST.get("Username")
    Password=request.POST.get("Password")
    
    if Username is not None and Password is not None:
        obj=siteuser(Username=Username,Password=Password)
        obj.save()
        return redirect("http://localhost:8000/")
        
    
        
    return render(request,"Home.html",{})
    
def homepage(request):
    return render(request,"Homepage.html",{})
    
    
    
def login_page(request):
   
    if request.session.get("U") is not None:
        return redirect("http://localhost:8000/home/")

        
    Username=request.POST.get("Username")
    Password=request.POST.get("Password")
    
    if Username is not None and Password is not None:
        
        obj=siteuser.objects.filter(Username=Username,Password=Password)
        if len(obj)>0:
            request.session["U"]=Username
            return redirect("http://localhost:8000/home/")
        else:
            return render(request,"Home2.html",{})
    else:
        pass
        
    return render(request,"Home2.html",{})
    
    
    
def logout(request):
    request.session["U"]=None
    return redirect("http://localhost:8000/")
    


    
    
    