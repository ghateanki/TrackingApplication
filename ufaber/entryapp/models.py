from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    task = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    start = models.TimeField()
    end = models.TimeField()


    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

# class task(models.Model):
#     description = models.CharField(max_length=255)
#     start = models.DateTimeField(auto_now_add=True, blank=True)
#     end = models.DateTimeField(blank=True)
#
#     def __str__(self):
#         return self.description + ' | ' + str(self.author)


    
    


