from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datePublished = models.DateTimeField(blank=True, null=True)
    dateCreated = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    title = models.CharField(max_length=200)

    def publish(self):
        self.datePublished = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title   
 