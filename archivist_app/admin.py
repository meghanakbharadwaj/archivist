from django.contrib import admin
from archivist_app.models import *
# Register your models here.
my_models = [Course_Provider,Domains,Course,Reviews,Keywords]

admin.site.register(my_models)