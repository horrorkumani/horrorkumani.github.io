from django.db import models
from django.urls import reverse #generate urls from url patterns
import uuid # required for primary key

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField(max_length=10000, help_text= 'Enter the content of the article')
    create_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])  # return url for each article id


