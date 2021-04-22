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


def profile(request, pk):
    contact=Contact.objects.get(id=pk)
    return render(request,'contact-profile.html',{'contact':contact})

def edit(request,pk):
    contact=Contact.objects.get(id=pk)
    if request.method=="POST":
        contact.full_name=request.POST['fullname']
        contact.relationship=request.POST['relationship']
        contact.phone_number=request.POST['phone-number']
        contact.email=request.POST['email']
        contact.address=request.POST['address']
        contact.save()
        Id=str(contact.id)
        return redirect('/profile/'+Id)
    return render(request,'edit.html',{'contact':contact})

def delete(request,pk):
    contact=Contact.objects.get(id=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('/')
    return render(request,'delete.html',{'contact':contact})