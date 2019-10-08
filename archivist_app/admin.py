from django.contrib import admin
from .models import Course_Provider,Image_Source,Domains,Reviews,Course
# Register your models here.
my_models = [Course_Provider,Image_Source,Domains,Reviews,Course]

admin.site.register(my_models)