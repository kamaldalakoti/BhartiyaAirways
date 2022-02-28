from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from airways import  views 

app_name = "Student"

urlpatterns = [
    
    # admin student page 
    path('' , views.Home , name="Home"),
    path('Home' , views.Home , name="Home"),
    path('About' , views.About , name="About"),
    path('Contact' , views.Contact , name="Contact"),
    path('Service' , views.Service , name="Service"),
    path('Current_opening' , views.Current_opening , name="Current_opening"),
   

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)