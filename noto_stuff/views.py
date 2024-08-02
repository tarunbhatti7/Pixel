from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Team ,Bugs
from django import forms
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.


def Bugs_in(requests):

    if requests.method == 'POST':
        data = requests.POST
        name = data.get('name')
        email = data.get('email')
        bug = data.get('bugs')
        image = requests.FILES.get('image')

        object = Bugs.objects.create(
                name = name ,
                email = email, 
                bug= bug,
                image = image,
            )
        
        object.save()
        # name='Thanks for Uploading'
        # message = f"We truly appreciate your effort and dedication in helping us improve our website {name}. It's because of thoughtful individuals like you that we can continue to grow and deliver a better service. " \
        #               f"Thank you for your contribution and for being an integral part of our community."
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [email]
        # send_mail(name, message, email_from, recipient_list )
        messages.info(requests,'thanks for reporting bug')
        
        return HttpResponseRedirect('/')
    else:
        return render(requests, 'report_Bugs.html')
