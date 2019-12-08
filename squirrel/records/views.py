from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Squirrel
from .forms import SquirrelForm

def index(request):
    return render(request,'records/index.html',{})

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'records/list.html', context)

def map(request):
    squirrels = Squirrel.objects.all()
    return render(request, 'records/map.html', {'squirrels':squirrels})


def edit_squirrel(request, squirrel_id):
    squirrel = Squirrel.objects.get(id=squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/records/list')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
        'form': form,
    }

    return render(request, 'records/edit.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records:list')

    else:
        form = SquirrelForm()

    context = {
        'form': form,
    }

    return render(request, 'records/add.html', context)

def stats(request):
    squirrels=Squirrel.objects
    squnumber=squirrels.count()
    amnumber=squirrels.filter(Shift='AM').count()
    pmnumber=squirrels.filter(Shift='PM').count()
    adultnumber=squirrels.filter(Age='Adult').count()
    junumber=squirrels.filter(Age='Juvenile').count()
    context={'squnumber':squnumber,'amnumber':amnumber,'pmnumber':pmnumber,'adultnumber':adultnumber,'junumber':junumber}
    return render(request, 'records/stats.html',context)

