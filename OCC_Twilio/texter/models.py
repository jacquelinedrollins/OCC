from django.db import models

# Create your models here.
import datetime
from django.utils import timezone


class Response(models.Model):
    phone = models.CharField(max_length=12)
    response = models.CharField(max_length=1)
    reply_date = models.DateTimeField('date published')
    def __str__(self):
        return self.phone + ' ' + self.response + ' ' + str(self.reply_date)
