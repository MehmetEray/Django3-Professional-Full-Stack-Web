from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User


# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class article(models.Model):
    picture = models.ImageField(upload_to='article_pictures')
    header = models.CharField(max_length=50)
    content = models.TextField()
    existed_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='header', unique=True)
    categories = models.ManyToManyField(category, related_name='article')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    class Meta:
        db_table = 'Article'
