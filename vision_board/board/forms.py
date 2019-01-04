from django import forms
from .models import Note

# old simple form, not connected to model Note:
# class NoteForm(forms.Form):
# 	title = forms.CharField(label='Title', max_length=50)
# 	text = forms.CharField(label='Text', max_length=250)
# 	picture = forms.FileField(required=False) 


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'picture']
        