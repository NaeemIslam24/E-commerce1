from django.shortcuts import render
from . models import *
# Create your views here.


def index(request):

    template = 'store1.html'

    products = Product1.objects.all()

    context = {
        'products': products
    }
    return render(request, template_name=template, context=context)


def cart(request):

    template = 'cart1.html'

    if request.user.is_authenticated:

        # user app to customer1 app by one to one relation
        customer = request.user.customer1

        order = Order1.objects.get(customer=customer, complete=False)

        items = order.orderitem1_set.all()

    context = {
        'order': customer,
        'items': items

    }
    return render(request, template_name=template, context=context)


def checkout(request):

    template = 'checkout1.html'

    context = {

    }
    return render(request, template_name=template, context=context)
