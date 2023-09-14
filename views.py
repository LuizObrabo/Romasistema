from django.shortcuts import render, redirect
from app.forms import NomesForm
from app.models import nomes
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = nomes.objects.filter(Nome_completo__icontains=search)
    else:
        data ['db'] = nomes.objects.all()
   # all = nomes.objects.all()
    #paginator = Paginator(all,5)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = NomesForm()
    return render(request, 'form.html', data)

def create(request):
    form = NomesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = nomes.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = nomes.objects.get(pk=pk)
    data['form'] = NomesForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = nomes.objects.get(pk=pk)
    form = NomesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')


def delete(request, pk):
    db = nomes.objects.get(pk=pk)
    db.delete()
    return redirect('home')




