from django.contrib import admin
from .models import Course_Provider,Image_Source,Domains,Reviews
# Register your models here.
my_models = [Course_Provider,Image_Source,Domains,Reviews]

admin.site.register(my_models)