# coding:utf-8
from django.db import models
# Create your models here.


class User(models.Model):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    datetime = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=30)
    image = models.ImageField(null=False, blank=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username
