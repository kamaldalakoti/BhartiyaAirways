from django.shortcuts import render

from bhartiya_airways.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


# Create your views here.

def Home(request):
    
    return render(request , 'index.html')


def About(request):

    return render(request , 'about.html')
    

def Contact(request):

    return render(request , 'contact.html')
    

def Service(request):
    if request.POST.get('query') =="QUERY":
            name = request.POST.get('form_name')
            email = request.POST.get('form_email')
            subject = request.POST.get('form_subject')
            message = request.POST.get('form_message')
            # form = {name,email,subject,message}
            # query_form(form_name=name,form_email=email,form_subject=subject,form_message=message).save()
            send_mail(subject, 
            message, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently = False)
            message = "Your message has been sucessfully submited"
            send_mail(subject, 
            message, EMAIL_HOST_USER, [email], fail_silently = False)

    return render(request , 'service.html')
def Current_opening(request):


    return render(request , 'current_opening.html')