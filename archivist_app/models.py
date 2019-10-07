from django.db import models

# Create your models here.
class Reviews(models.Model):
    course_id = models.IntegerField()
    review = models.TextField
    review_source = models.CharField(max_length = 20)

class Domains(models.Model):
    domain_name = models.CharField(max_length= 30)
 
class Course_Provider(models.Model):
    provider_name = models.CharField(max_length= 50)
    provider_link = models.URLField()
    provider_logo = models.ImageField()

class Image_Source(models.Model):
    keyword = models.CharField(max_length= 30)
    logo = models.ImageField(upload_to='logos')

class upvote(models.Model):
    user_id = models.IntegerField()
    course_id = models.IntegerField()