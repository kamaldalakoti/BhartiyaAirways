from re import T
from tkinter.tix import Select
from django.db import models
from pyparsing import null_debug_action

# Create your models here.
class applied(models.Model):
    Name = models.CharField(max_length=200 , null=True)
    Email = models.EmailField(max_length=200 , null=True)
    Mobile = models.CharField(max_length=200 , null=True)
    Address = models.CharField(max_length=200 , null=True)
    City = models.CharField(max_length=200 , null=True)
    Select_reference = [
    ('Fb', 'Fackbook'),
    ('Insta', 'Instagram'),
    ('Youtube', 'Youtube'),
    ('Website', 'Website'),
    ('Others', 'Others'),

]
    reference = models.CharField(max_length=20, choices=Select_reference , null=True)
    trm = models.BooleanField(default=False)
