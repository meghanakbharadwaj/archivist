from django.db import models

# Create your models here.


class Domains(models.Model):
    domain_name = models.CharField(max_length= 30)

    def __str__(self):
        return self.domain_name
 
class Course_Provider(models.Model):
    provider_name = models.CharField(max_length= 50)
    provider_link = models.URLField()
    provider_logo = models.ImageField(upload_to='provider_logos')

    def __str__(self):
        return self.provider_name

class Keywords(models.Model):
    keyword = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='logos')
    domain = models.ForeignKey(Domains,on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.keyword,self.domain)

class Course(models.Model):
    keyword = models.ForeignKey(Keywords,on_delete=models.CASCADE)
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

class Reviews(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    review = models.TextField
    review_source = models.CharField(max_length = 20)

    def __str__(self):
        return self.review
