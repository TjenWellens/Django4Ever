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
    def __init__(self, i):
        self.guid = i
        self.title = "Note nr. %d" % i
        self.contentLengtr = i * 100
