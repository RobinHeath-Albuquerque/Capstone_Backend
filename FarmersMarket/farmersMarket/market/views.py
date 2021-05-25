from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Market, Employee, Grower, Buyer
from django.urls import reverse

def index(request):
    all_markets = Market.objects.all()
    context = {
        'all_markets': all_markets
    }
    return render(request, 'market/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        time = request.POST.get('time')
        location = request.POST.get('location')
        new_market = Market(name=name, time=time, location=location)
        new_market.save()
        return HttpResponseRedirect(reverse('market:index'))
    else:
        return render(request, 'market/create.html')
