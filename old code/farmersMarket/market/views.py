
from django.apps import apps
from django.db.models.signals import post_save
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render
from django.template import context
from datetime import date
import datetime

from .models import Buyer, Grower
from django.urls import reverse
import decimal


def index(request):
    # get the logged in user within any view function
    user = request.user
    all_buyers = Buyer.objects.all()
    context = {
        'all_buyers': all_buyers
    }

    print(user)
    return render(request, 'buyers/index.html', context)


def account(request):
    if request.method == 'GET':
        user = request.user
        Buyer = apps.get_model('buyer.Buyer')
        buyer = Buyer.objects.get(user_id=user.id)
        context = {
            'buyer': buyer
        }

        return render(request, 'buyer/account.html', context)
    else:
        return HttpResponseRedirect(reverse('buyer:index'))


def search_for_seller(request):
    if request.method == 'POST':
        user = request.user
        buyer = Buyer.objects.get(user_id=user.id)
        buyer.search_for_seller = request.POST.get('search_for_seller')
        Buyer.save()

        return HttpResponseRedirect(reverse('buyer:index'))
    else:
        return render(request, 'buyer/search_for_seller')

def search_for_product(request):
    if request.method == 'POST':
        user = request.user
        buyer = Buyer.objects.get(user_id=user.id)
        buyer.search_for_product = request.POST.get('search_for_product')
        buyer.save()
        return HttpResponseRedirect(reverse('buyer:index'))
    else:
        return render(request, 'buyer/search_for_product')


def search_for_recipe(request):
    if request.method == 'POST':
        user = request.user
        buyer = Buyer.objects.get(user_id=user.id)
        buyer.search_for_recipe = request.POST.get('search_for_recipe')
        buyer.save()
        return HttpResponseRedirect(reverse('buyer:index'))
    else:
        return render(request, 'buyer/search_for_recipe')



40



def create(request):
    if request.method == 'POST':
        user = request.user
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        new_buyer = Buyer(fname=fname, lname=lname, uname=uname, password=password)
        new_buyer.user_id = user.id
        new_buyer.save()
        return HttpResponseRedirect(reverse('buyer:index'))
    else:
        return render(request, 'buyer/create.html')




