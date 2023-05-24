from django.shortcuts import render

from a3h1collegestore.models import Message
from order.models import Order


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        messages=Message(name=name,email=email,subject=subject,message=message)
        messages.save()
        from django.contrib import messages
        messages.success(request, 'Message sent successfully')
    return render(request,'contact.html')
