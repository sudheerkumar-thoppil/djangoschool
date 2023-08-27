from django.shortcuts import render,HttpResponse
from .models import Studentregister

# Create your views here.
def register(request):
    if request.method=="POST":
        if request.POST.get('name') and request.POST.get('standard') and request.POST.get('phone'):
            newstudent =Studentregister()
            newstudent.name =request.POST.get('name')
            newstudent.standard = request.POST.get('standard')
            newstudent.phone = request.POST.get('phone')
            newstudent.save()
            return render(request,'register.html')
        else:
            return render(request,'register.html')
    else:
        return render(request,'register.html')



def viewregister(request):

    sregister=Studentregister.objects.all()
    return render(request,'viewregister.html',{'sregister':sregister})


def namesearch(request):
    nameregister=Studentregister.objects.filter()
    return render(request,'namesearch.html',{'nameregister':nameregister})

def findname(request):
    findregister=Studentregister.objects.all()
    return render(request,'find.html',{'findregister':findregister})

