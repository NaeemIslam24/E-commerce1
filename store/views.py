from django.shortcuts import render
from . models import *
# Create your views here.
from django.http import JsonResponse
import json

def index(request):
    template = 'store.html'
    product = Product.objects.all()
    

    context = {
        'products': product,

    }

    return render(request, template_name=template, context=context)


def cart(request):
    template = 'cart.html'
    if request.user.is_authenticated:
        customer = request.user.customer  # user app to customer app by one to one relation

        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        cartitem = order.get_cart_Item_total

        items = order.orderitem_set.all()  # it will return exact user's order item
        # items = OrderItem.objects.all() # it will return all user's order item
    else:
        items = []
        # when user not authenticated it works
        order = {'get_cart_Item_total': 0, 'get_cart_total': 0, 'shipping': False}

        cartitem = order['get_cart_Item_total']

    context = {
        'items': items,
        'order': order,
        'cartitem': cartitem,
    }

    return render(request, template_name=template, context=context)



def checkout(request):
    template = 'checkout.html'
    if request.user.is_authenticated:
        customer = request.user.customer  # user app to customer app by one to one relation

        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

        items = order.orderitem_set.all()  # it will return exact user's order item
        # items = OrderItem.objects.all() # it will return all user's order item
    else:
        items = []
        # when user not authenticated it works
        order = {'get_cart_Item_total': 0, 'get_cart_total': 0, 'shipping': False}

    context = {
        'items': items,
        'order': order,
    }

    return render(request, template_name=template, context=context)

def updateItem(request):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']


    customer = request.user.customer

    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
    
    orderitem, created = OrderItem.objects.get_or_create(order = order, product = product)
    print('before if',orderitem.quantity)
    if action == 'add':

        orderitem.quantity = orderitem.quantity + 1

    elif action == 'remove':

        orderitem.quantity = orderitem.quantity - 1

    orderitem.save()

    if orderitem.quantity <= 0:

        orderitem.delete()

      
    

    return JsonResponse('Item was added', safe=False)