from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        return HttpResponse("<h1>Thanks for contact</h1>")



    return render(request,'index.html')