# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Base._title'
        db.add_column('project_base', '_title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)

        # Adding field 'Base._date'
        db.add_column('project_base', '_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 10, 25, 0, 0)),
                      keep_default=False)

        # Adding field 'Base._lastModified'
        db.add_column('project_base', '_lastModified',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 10, 25, 0, 0)),
                      keep_default=False)

        # Adding field 'Base.slug'
        db.add_column('project_base', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Base._title'
        db.delete_column('project_base', '_title')

        # Deleting field 'Base._date'
        db.delete_column('project_base', '_date')

        # Deleting field 'Base._lastModified'
        db.delete_column('project_base', '_lastModified')

        # Deleting field 'Base.slug'
        db.delete_column('project_base', 'slug')


    models = {
        'project.base': {
            'Meta': {'object_name': 'Base'},
            '_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 25, 0, 0)'}),
            '_lastModified': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 25, 0, 0)'}),
            '_title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['project']