from pickle import NONE

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Market, Employee, Grower, Buyer
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    return render(request, 'registration/index.html')


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or NONE)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'registration/index.html')
        context['form'] = form
        return render(request, 'registration/sign_up.html', context)


#def index(request):
    #all_markets = Market.objects.all()

    #context = {
       # 'all_markets': all_markets
   # }
   # return render(request, 'market/index.html', context)


#def create(request):

   # if request.method == 'POST':
        #name = request.POST.get('name')
        #time = request.POST.get('time')
        #location = request.POST.get('location')
        #new_market = Market(name=name, time=time, location=location)
        #new_market.save()
       # return HttpResponseRedirect(reverse('market:index'))
    #else:
        #return render(request, 'market/create.html'



