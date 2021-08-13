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
        customer = request.user.customer  # user app to customer app by one to one relation
        print('---------store----------')
        print(customer)

        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

        items = order.orderitem_set.all()  # it will return exact user's order item
        # items = OrderItem.objects.all() # it will return all user's order item
    else:
        items = []
        # when user not authenticated it works
        order = {'get_cart_Item_total': 0, 'get_cart_total': 0}

    context = {
        'items': items,
        'order': order,
    }

    return render(request, template_name=template, context=context)


def checkout(request):
    template = 'checkout.html'

    context = {}

    return render(request, template_name=template, context=context)
