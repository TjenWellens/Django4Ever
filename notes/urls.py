from django.conf.urls import *
from notes.views import view_notes, note_number, view_note_list

urlpatterns = patterns('',
                       (r'^$', view_notes),
                       (r'^(\d+)/$', note_number),
                       (r'^list/$', view_note_list),
)