#coding: utf-8
from django.contrib import admin
from models import Journal

class AdminJournal(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Journal, AdminJournal)
