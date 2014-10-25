# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Journal'
        db.create_table('journal_journal', (
            ('base_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['project.Base'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('intro', self.gf('django.db.models.fields.TextField')()),
            ('content', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('journal', ['Journal'])


    def backwards(self, orm):
        # Deleting model 'Journal'
        db.delete_table('journal_journal')


    models = {
        'journal.journal': {
            'Meta': {'object_name': 'Journal', '_ormbases': ['project.Base']},
            'base_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['project.Base']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'project.base': {
            'Meta': {'object_name': 'Base'},
            '_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 25, 0, 0)'}),
            '_lastModified': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 25, 0, 0)'}),
            '_title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['journal']