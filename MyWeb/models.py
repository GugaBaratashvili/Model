from django.db import models
from django.utils import timezone
from django.urls import reverse



class Numsum(models.Model):
    #author = models.ForeignKey('auth.User', 'on_delete')
    num1 = models.IntegerField(blank=True, null=True)
    num2 = models.IntegerField(blank=True, null=True)
    num3 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.num1, self.num2
