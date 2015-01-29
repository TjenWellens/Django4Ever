from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes import urls as note_urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'notes/', include(note_urls)),
)
