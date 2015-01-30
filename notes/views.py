from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from notes.forms import UpdateNoteForm


def view_note_list(request):
    note_list = (DummyNote(i) for i in range(1, 11))
    return render(request, 'notelist.html', {'note_list': note_list})


def update_note_get(request, guid):
    note = DummyNote(int(guid))
    form = UpdateNoteForm(
        initial={
            'guid': note.guid,
            'title': note.title,
            'content': note.content,
        }
    )
    return render(request, 'note_edit.html', {'form': form})


def update_note_post(request):
    form = UpdateNoteForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        guid = cd['guid']
        title = cd['title']
        content = cd['content']
        return HttpResponse('guid: %s<br>title: %s<br>content: %s<br>' % (guid, title, content,))


class DummyNote(object):
    def __init__(self, guid):
        self.guid = guid
        self.title = "Note nr. %d" % guid
        self.contentLengtr = guid * 100
        self.content = "Note nr. %d's content..." % guid