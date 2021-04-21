from django.shortcuts import render,redirect
from .models import Contact

def index(request):
    contacts=Contact.objects.all()
    return render(request,'index.html',{'contacts':contacts})

def addContacts(request):

    if request.method=="POST":
        name=request.POST['fullname'],
        relationship=request.POST['relationship'],
        phone=request.POST['phone-number'],
        address=request.POST['address'],
        email=request.POST['email']
        user=Contact(full_name=name,relationship=relationship,phone_number=phone,address=address,email=email)
        user.save()
        return redirect('/')

    return render(request,'new.html')