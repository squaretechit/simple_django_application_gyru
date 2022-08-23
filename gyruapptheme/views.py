from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import auth, User


class IndexView(TemplateView):

    def home(request):
        return render(request, 'home.html')

    def about(request):
        return render(request, 'about.html')

    def contact(request):
        if request.method == 'POST':
            full_name = request.POST['name']
            Email_Address = request.POST['email']
            subject = request.POST['subject']
            Message = request.POST['text']
            mail = (f"My name is {full_name}. My Email is {Email_Address}. My Subject is {subject}, My message is {Message}")
            send_mail('Message from gyru.co.uk', mail, 'admin@gyru.co.uk', ['gyruapp@gmail.com'], fail_silently=False,)
            messages.info(request, 'Thank you! We will contact you soon.')
            return render(request, 'contact.html')   
        else:
            return render(request, 'contact.html')

    def policy(request):
        return render(request, 'privacy-policy.html')
