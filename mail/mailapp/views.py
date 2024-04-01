from django.shortcuts import render,redirect
from .utils import mail
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def home(request):
    home_dict = {"title" : "Home"}
    if request.method == 'POST':
        # Assuming you have a form with fields: subject, message, recipient
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        recipient = request.POST.get('recipient', '')

        # Sending email
        mail(subject, message, recipient)
        home_dict.update({"success" : "Mail Successfully Sent!","task" : True})
        # Redirecting to a success page
        return render(request, 'email.html',context=home_dict)
    
    # If method is not POST, render the form
    return render(request, 'email.html',context=home_dict)
