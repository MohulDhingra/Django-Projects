from django.shortcuts import render
from .models import item

# Create your views here.
def homepage(request):
    q=request.POST.get("q")
    if q is not None:
        obj=item.objects.filter(Title__icontains=q)
        if len(obj)>0:
            return render(request,"home.html",{'x':obj})
        else:
            return render(request,"home.html",{'x':obj})
    
    
    else:
        obj=item.objects.all()
        return render(request,"home.html",{'x':obj})
