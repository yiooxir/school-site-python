# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Children'
        db.create_table('children_children', (
            ('base_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['project.Base'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('intro', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='images/no-photo.jpg', max_length=100)),
        ))
        db.send_create_signal('children', ['Children'])


    def backwards(self, orm):
        # Deleting model 'Children'
        db.delete_table('children_children')


    models = {
        'children.children': {
            'Meta': {'object_name': 'Children', '_ormbases': ['project.Base']},
            'base_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['project.Base']", 'unique': 'True', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/no-photo.jpg'", 'max_length': '100'}),
            'intro': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'project.base': {
            'Meta': {'object_name': 'Base'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 25, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastModified': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 25, 0, 0)'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        }
    }

    complete_apps = ['children']