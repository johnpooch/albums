from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import addMusicForm
from .models import Title

# Create your views here.
def get_index(request):
    titles = Title.objects.all()
    return render(request, "home/index.html", {"titles" : titles})
    
def add_music(request, pk=None):
    title = get_object_or_404(Title, pk=pk) if pk else None
    if request.method == "POST":
        form = addMusicForm(request.POST, request.FILES, instance=title)
        if form.is_valid():
            title = form.save(commit=False)
            title.owner = request.user
            title.save()
            return redirect('home/index')
    else:
        form = addMusicForm(instance=title)
    return render(request, "home/add_music.html", {'form': form})
