from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404


def view_notes(request):
    return HttpResponse("Hello notes")


def note_number(request, number):
    return HttpResponse("Hello %s" % number)


def view_note_list(request):
    note_list = (DummyNote(i) for i in range(1, 11))
    return render(request, 'notelist.html', {'note_list': note_list})


class DummyNote(object):
    def __init__(self, guid):
        self.guid = guid
        self.title = "Note nr. %d" % guid
        self.contentLengtr = guid * 100
        self.content = "Note nr. %d's content..." % guid


dev_token = "S=s1:U=9030d:E=1523c272e4a:C=14ae475ff50:P=1cd:A=en-devtoken:V=2:H=df8bb61301f2397ae57baaf5d4185877"



# views (general splitting code)
def method_splitter(request, *args, **kwargs):
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)
    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404


from notes.forms import UpdateNoteForm


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