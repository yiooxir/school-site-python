#coding: utf-8

from django.db import models
from datetime import datetime


class Base(models.Model):
    title = models.CharField(max_length=250, blank=True)
    date = models.DateField(default=datetime.today())
    lastModified = models.DateField(default=datetime.today())
    slug = models.SlugField(max_length=100, blank=True)

    def get_url(self):
        return '/%s/' % self.slug

    def save(self, *args, **kwargs):
        self._lastModified = datetime.today()
        super(Base, self).save()