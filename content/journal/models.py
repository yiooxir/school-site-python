#coding: utf-8

from project.models import Base
from django.db import models
from tinymce import models as tinymce_models


class Journal(Base):
    name = models.CharField(max_length=250)
    intro = models.TextField()
    content = tinymce_models.HTMLField(blank=True)
    image = models.ImageField(upload_to='journal-img', blank=True)

    def __unicode__(self):
        return self.name

    def get_article_url(self):
        return '/journal/%s/' % self.name