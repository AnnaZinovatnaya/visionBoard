from django.shortcuts import render
from .models import Note
from .forms import NoteForm
from django.http import HttpResponseRedirect


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