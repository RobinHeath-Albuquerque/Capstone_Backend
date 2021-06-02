from django.shortcuts import render
from django.http import HttpResponse
from .models import Market, Grower, Product, ProductCategory, Shopper

def index(request):
    all_markets = Market.objects.all()
    context = {
        'all_markets': all_markets
    }
    return render(request, 'markets/index.html', context)

# Create your views here.
