from django.conf import settings
from django.shortcuts import render
from django.contrib import messages



from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.template import loader


from content.forms import ContactForm
from .models import *

# Create your views here.
def home(request):
    profile = Profile.objects.first()
    about = About.objects.first()
    skill = Skill.objects.all()
    social = SocialMedia.objects.first()
    
    webdev_1 = Webdevelopment.objects.all()[0]
    webdev_2 = Webdevelopment.objects.all()[1]
    
    personal_one = Personal.objects.all()[0]
    personal_2 = Personal.objects.all()[1]
    
    selfphoto_1 = SefPhotograph.objects.all()[0]
    selfphoto_2 = SefPhotograph.objects.all()[1]
    exp = Experience.objects.all()
    
    edu = Education.objects.all()
    
    #form
    form = ContactForm()
    
    context ={'profile': profile,
              'about' : about,
              'skill' : skill,
              'social' : social,
              'personal_1': personal_one,
              'personal_2': personal_2,
              'selfphoto1': selfphoto_1,
              'selfphoto2': selfphoto_2,
              'edu': edu,
              'exp' : exp,
              'webdev_1': webdev_1,
              'webdev_2': webdev_2,
              'form' : form
              }
    
    return render(request , 'content/index.html',context)


#2nd view contact
def MailContact(request):
    if request.method == "POST": #here inknow the form is submited
        
        form = ContactForm(request.POST) # form
        
        if form.is_valid():
            #data is instancce
            data = Contact() #our contact model
            
            data.fullname = form.cleaned_data['fullname']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            
            data.save() # here we save the data in the database

            fullname = form.cleaned_data['fullname']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['shivamsharma38391@gmail.com']
            
            html = loader.render_to_string(
                'content/email.html' ,
                {
                    'subject': subject,
                    'message': message,
                    'fullname': fullname,
                    'email': email,
                }
            )
            
            
            if subject and message and email_from and recipient_list and html:
                try:
                    send_mail(subject, message, email_from, recipient_list, html_message= html, fail_silently=False)
                except:
                    messages.error(request,"Cannot send mail right now, Try again later")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                
                messages.success(request,"Message sent successfully")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            else:
                messages.error(request,"Please! Make sure all fields are entered and valid.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request,"Please! Make sure all fields are entered and valid.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        

def Adminpanel(request):
    
    return HttpResponseRedirect("/admin/")

            
        
