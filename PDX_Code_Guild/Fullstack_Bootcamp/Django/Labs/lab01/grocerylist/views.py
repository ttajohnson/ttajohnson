from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import GroceryItem

def index(request):
    latest_grocerylist = GroceryItem.objects.order_by('-date_created')
    not_complete = latest_grocerylist.filter(is_done = False)
    complete = latest_grocerylist.filter(is_done = True)
    # grocery_item = get_object_or_404(GroceryItem, pk=grocery_item.id)
    context = {
        'latest_grocerylist': latest_grocerylist,
        'not_complete': not_complete,
        'complete': complete,
        # 'grocery_item':grocery_item,
    }
    return render(request, 'grocerylist/index.html', context)

def create(request):
    GroceryItem(description = request.POST['description']).save()
    return HttpResponseRedirect(reverse('grocerylist:index'))

def complete(request, grocery_item_id):
    # if request.method == 'post':
    print(grocery_item_id)
    grocery_item = get_object_or_404(GroceryItem, pk=grocery_item_id)
    if grocery_item.is_done == False:
        grocery_item.is_done = True
    else: 
        grocery_item.is_done = False
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocerylist:index'))

def delete(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, pk=grocery_item_id)
    if request.method == "POST":
        grocery_item.delete()
    return HttpResponseRedirect(reverse('grocerylist:index'))

