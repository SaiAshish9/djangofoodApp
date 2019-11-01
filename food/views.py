from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
from django.shortcuts import render

# Create your views here.
def index(req):
    item_list=Item.objects.all()
    template = loader.get_template('food/index.html')
    context ={
       'item_list': item_list,
    }
    # return HttpResponse(template.render(context,req))
    return render(req, 'food/index.html ',context)
def item(request):
    return HttpResponse('This is an item view ')

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    # return HttpResponse("This is item no/id: %s"%item_id)
    return render(request, 'food/detail.html ',context)