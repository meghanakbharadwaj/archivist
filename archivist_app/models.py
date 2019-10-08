from django.db import models

# Create your models here.
class Reviews(models.Model):
    course_id = models.IntegerField()
    review = models.TextField
    review_source = models.CharField(max_length = 20)

class Domains(models.Model):
    domain_name = models.CharField(max_length= 30)

    def __str__(self):
        return self.domain_name
 
class Course_Provider(models.Model):
    provider_name = models.CharField(max_length= 50)
    provider_link = models.URLField()
    provider_logo = models.ImageField()

    def __str__(self):
        return self.provider_name

class Image_Source(models.Model):
    keyword = models.CharField(max_length= 30)
    logo = models.ImageField(upload_to='logos')

    def __str__(self):
        return self.keyword

class upvote(models.Model):
    user_id = models.IntegerField()
    course_id = models.IntegerField()

class Course(models.Model):
    keyword = models.CharField(max_length=30)
    domain = models.ForeignKey(Domains,on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    provider = models.ForeignKey(Course_Provider, on_delete = models.CASCADE)
    course_link = models.URLField()
    course_type = models.CharField(max_length=10,choices=(('Paid','Paid'),('Not Paid','Not Paid')))
    Medium = models.CharField(max_length=20,choices=(('Video','Video'),('Documents','Documents')))
    description = models.TextField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return "%s - %s" % (self.title,self.provider)