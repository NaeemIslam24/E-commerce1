from django.shortcuts import render
from . models import *
from . forms import MathForm

# Create your views here.


def index(request):
    template = 'maths.html'

    if request.method == 'POST':

       math = Math.objects.get(id=1)

       form = MathForm(request.POST, instance=math)

       form.save()

    else:
        math = Math.objects.get(id=1)

        form = MathForm(instance=math)

    context = {

        'math': math,
        'form': form,

    }

    return render(request, template_name=template, context=context)
