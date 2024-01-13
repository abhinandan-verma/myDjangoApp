from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from food.models import Item


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)


def item(request):
    return HttpResponse("This is an item view")


def food(request):
    return HttpResponse("This is an food view")


def order(request):
    return HttpResponse("<h1>This is an Order view</h1><br>This is Next Line")
