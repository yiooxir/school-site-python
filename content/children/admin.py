#coding: utf-8
from django.contrib import admin
from models import Children

class AdminChildren(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Children, AdminChildren)