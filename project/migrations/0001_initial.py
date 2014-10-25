# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Base'
        db.create_table('project_base', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('project', ['Base'])


    def backwards(self, orm):
        # Deleting model 'Base'
        db.delete_table('project_base')


    models = {
        'project.base': {
            'Meta': {'object_name': 'Base'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['project']