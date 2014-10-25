from django.conf.urls import patterns, include, url

urlpatterns = patterns('content.journal.view',
                       url(r'/$', 'journal_list'),
                       url(r'([^/]+)/$', 'journal_article'),
                       )
