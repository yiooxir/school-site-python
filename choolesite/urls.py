from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
import settings


from django.contrib import admin
admin.autodiscover()


urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
                        url(r'^admin_tools/', include('admin_tools.urls')),
                        url(r'^admin/', include(admin.site.urls)),
                        )
urlpatterns += patterns('',
                        (r'^tinymce/',include('tinymce.urls')),
                        (r'^admin/filebrowser/', include('filebrowser.urls')),
                        )

urlpatterns += patterns('',
                        url(r'^$', 'content.views.index'),
                        )