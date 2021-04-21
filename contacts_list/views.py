from django.shortcuts import render,redirect
from .models import Contact

def index(request):
    contacts=Contact.objects.all()
    return render(request,'index.html',{'contacts':contacts})

def addContacts(request):

    if request.method=="POST":
        user=Contact(
            full_name=request.POST['fullname'],
            relationship=request.POST['relationship'],
            phone_number=request.POST['phone-number'],
            email=request.POST['email'],
            address=request.POST['address'],)
        user.save()
        return redirect('/')

    return render(request,'new.html')