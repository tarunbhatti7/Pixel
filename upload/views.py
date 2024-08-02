from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Post_first,Post_second,Post_third,Post_fourth
from django import forms
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

SUBJECT_CHOICE=[
    ('physics','physics'),
    ('chemistry','chemistry'),
    ('maths','maths'),

]

class Upload_form(forms.Form):
    name=forms.CharField(max_length=20,widget=forms.Select(choices=SUBJECT_CHOICE,attrs={'class':"form-control",'id':"exampleFormControlSelect1",'style': 'width:80%; margin:40px 0 40px 0'}))
    title=forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control','id':'exampleInputName','placeholder':'Title','style': 'width:80%'}))
    dis=forms.CharField(max_length=240, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Discription','style': 'margin:0 0 40px 0; width:80%; font-family:Montserrat, sans-serif; background-color:#EBECF0; text-shadow: 1px 1px 1px #FFF;text-shadow: 1px 1px 0 #FFF;box-shadow:  inset 2px 2px 5px #BABECC, inset -5px -5px 10px #FFF;'}))
    file=forms.FileField()
    def __init__(self, *args, **kwargs):
        super(Upload_form, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'id':'dropzone-file','style':'width:80%'})



def Show_view_ist(requests):
    return render(requests,'detail_ist.html')

def Post_view_ist(requests):
    post_view_ist=Post_first.objects.all()
    return JsonResponse({"data":list(post_view_ist.values())})

def Show_view_sec(requests):      
    return render(requests,'detail_sec.html')

def Post_view_sec(requests):
    post_view_sec=Post_second.objects.all()
    return JsonResponse({"data":list(post_view_sec.values())})

def Show_view_thir(requests):
    return render(requests,'detail_thir.html')

def Post_view_thir(requests):
    post_view_thir=Post_third.objects.all()
    return JsonResponse({"data":list(post_view_thir.values())})

def Show_view_four(requests):
    return render(requests,'detail_four.html')

def Post_view_four(requests):
    post_view_four=Post_fourth.objects.all()
    return JsonResponse({"data":list(post_view_four.values())})

def Select_comps(requests):
    return render(requests,'select_comps.html')

def Upload(requests):
    return render(requests,'upload.html')

@login_required
def Upload_view_ist(requests):
    if requests.method=='POST':
        form=Upload_form(requests.POST,requests.FILES)
        if form.is_valid():
            object=Post_first.objects.create(
            name=form.cleaned_data['name'],
            title=form.cleaned_data['title'],
            dis=form.cleaned_data['dis'],
            file=form.cleaned_data['file'],
            auname=requests.user.username,
            author=requests.user
            )
            object.save()
            messages.error(requests ,'uploaded')
            return HttpResponseRedirect('/detail_ist')
        else:
            return render(requests,'upload_ist.html',{'form':form})
    return render(requests,'upload_ist.html',{'form':Upload_form()})

@login_required
def Upload_view_sec(requests):
    if requests.method=='POST':
        form=Upload_form(requests.POST,requests.FILES)
        if form.is_valid():
            object=Post_second.objects.create(
            name=form.cleaned_data['name'],
            title=form.cleaned_data['title'],
            dis=form.cleaned_data['dis'],
            file=form.cleaned_data['file'],
            auname=requests.user.username,
            author=requests.user
             )
            object.save()
            messages.error(requests ,'uploaded')
            return HttpResponseRedirect('/detail_sec')
        else:
            return render(requests,'upload_sec.html',{'form':form})
    else:
        return render(requests,'upload_sec.html',{'form':Upload_form()})

@login_required
def Upload_view_thir(requests):
    if requests.method=='POST':
        form=Upload_form(requests.POST,requests.FILES)
        if form.is_valid():
            object=Post_third.objects.create(
            name=form.cleaned_data['name'],
            title=form.cleaned_data['title'],
            dis=form.cleaned_data['dis'],
            file=form.cleaned_data['file'],
            auname=requests.user.username,
            author=requests.user
             )
            object.save()
            messages.error(requests ,'uploaded')
            return HttpResponseRedirect('/detail_thir')
        else:
            return render(requests,'upload_thir.html',{'form':form})
    else:
        return render(requests,'upload_thir.html',{'form':Upload_form()})
    
@login_required
def Upload_view_four(requests):
    if requests.method=='POST':
        form=Upload_form(requests.POST,requests.FILES)
        if form.is_valid():
            object=Post_fourth.objects.create(
            name=form.cleaned_data['name'],
            title=form.cleaned_data['title'],
            dis=form.cleaned_data['dis'],
            file=form.cleaned_data['file'],
            auname=requests.user.username,
            author=requests.user
             )
            object.save()
            messages.error(requests ,'uploaded')
            return HttpResponseRedirect('/detail_thir')
        else:
            return render(requests,'upload_thir.html',{'form':form})
    else:
        return render(requests,'upload_thir.html',{'form':Upload_form()})
    
