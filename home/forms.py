from django import forms
from .models import Title

class addMusicForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ('release_title', 'artist', 'genres', 'image', 'published_date')
