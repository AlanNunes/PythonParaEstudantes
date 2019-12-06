from django.shortcuts import render, redirect
from django.http import HttpResponse
from filme.models import Filmes
from .forms import FormFilme

# Create your views here.
def filme_list(request):
    filmes = Filmes.objects.all()
    template_name = 'filme_list.html'
    context = {
        'filmes': filmes,
    }
    return render(request, template_name, context)

def filme_new(request):
    if request.method == "POST":
        form= FormFilme(request.POST)
        if form.is_valid:
            form.save()
            return redirect('filme_list')
    else:
        form= FormFilme()
    template_name ='filme_new.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)

def filme_edit(request, pk):
    filme = Filmes.objects.get(pk=pk)
    if request.method == 'POST':
        form= FormFilme(request.POST, instance=filme)
        if form.is_valid:
            form.save()
            return redirect('filme_list')
    else:
        form = FormFilme(instance=filme)
    template_name = 'filme_edit.html'
    context={
        'form': form,
        'pk': pk,
    }
    return render(request, template_name, context)

def filme_delete(request, pk):
    filme = Filmes.objects.get(pk=pk)
    filme.delete()
    return redirect('filme_list')