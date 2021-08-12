from django.shortcuts import render
from . models import *
# Create your views here.


def index(request):
    template = 'store.html'
    product = Product.objects.all()

    context = {
        'products': product
    }

    return render(request, template_name=template, context=context)


def cart(request):
    template = 'cart.html'
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context = {
        'items': items,
        'order': order,
    }

    return render(request, template_name=template, context=context)


def checkout(request):
    template = 'checkout.html'

    context = {}

    return render(request, template_name=template, context=context)
