#coding: utf-8

from project.models import Base
from django.db import models
from tinymce import models as tinymce_models


class Children(Base):
    name = models.CharField(max_length=250)
    intro = models.TextField()
    image = models.ImageField(upload_to='children-img', default='images/no-photo.jpg')

    def __unicode__(self):
        return self.name

    def get_url(self):
        return '/children/%s/' % self.name