from django.urls import path

from content.models import Contact
from .import views

urlpatterns = [
    path('',views.home , name= 'index' ),
    path("contact/" , views.MailContact, name = "contact"),
    path('admin/' , views.Adminpanel, name='admin')
]
