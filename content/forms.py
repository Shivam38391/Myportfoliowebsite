from dataclasses import field
from email import message

from django import forms
from django.forms import ModelForm

from content.models import Contact  #our model

class ContactForm(forms.ModelForm):
    #id and name
    fullname = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required= True)
    subject = forms.CharField(max_length=100, required= True)
    message = forms.CharField(required=True, widget=forms.Textarea)
    
    class Meta:
        model = Contact
        
        fields = "__all__"
        
        
    # to use the html class in django form we use init method
    def __init__(self, *args, **kwargs):   
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['fullname'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['fullname'].widget.attrs['class'] = "form-control"
        
        self.fields['email'].widget.attrs['placeholder'] = "E-mail"
        self.fields['email'].widget.attrs['class'] = "form-control"
        
        self.fields['subject'].widget.attrs['placeholder'] = "Subject"
        self.fields['subject'].widget.attrs['class'] = "form-control"
        
        self.fields['message'].widget.attrs['placeholder'] = "Your Message"
        self.fields['message'].widget.attrs['class'] = "form-control"
        
        

    