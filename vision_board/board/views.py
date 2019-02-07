from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from .models import Note
from .forms import NoteForm
from .serializers import NoteSerializer

def home(request):
    all_notes = Note.objects.all()
    return render(request, "board.html", context={'all_notes' : all_notes})


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():

            #note = Note()
            #note.title = form.cleaned_data['title']
            #note.text = form.cleaned_data['text']
            #contents = request.FILES['picture'].read()
            #note.picture = contents
            #note.save()
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = NoteForm()
        return render(request, "addNote.html", context={'note_form' : form})


def delete_note(request, note_id):
	note = Note.objects.get(pk=note_id)
	note.delete()
	return HttpResponseRedirect('/')



class NotesList(APIView):
    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many = True)
        return Response(serializer.data)
