from django.db import models
from django.conf import settings
from archivist_app.models import Course

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user.username)
    
    