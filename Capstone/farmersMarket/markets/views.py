from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Market, Grower, Product, ProductCategory, Shopper


def index(request):
    all_markets = Market.objects.all()
    context = {
        'all_markets': all_markets
    }
    return render(request, 'markets/index.html', context)


# Create your views here.

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company_name = request.POST.get('company')
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        new_grower = Grower(name=name, company_name=company_name, user_name=user_name, password=password)
        new_grower.save()
        return HttpResponseRedirect(reverse('markets.index'))
    else:
        return render(request, 'markets/create.html')
