from django.conf.urls import *
from notes import views

urlpatterns = patterns('',
                       (r'^$', views.view_note_list),
                       (r'^(\d+)/$', views.note_number),
                       (r'^list/$', views.view_note_list),
                       (r'^update/$', views.update_note_post),
                       (r'^update/(\d*)$', views.update_note_get),
)