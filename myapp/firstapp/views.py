from django.shortcuts import render
from django.http import HttpResponse


import math
# Create your views here.


def pagina2(request, values):

    try:
        delta = (pow(values[1], 2)) - (4 * values[0] * values[2])

        if delta < 0:

            return render(request, 'index2.html', {'menor': delta})

        elif delta == 0:

            x = (-values[1] + 0) / (2 * values[0])
            return render(request, 'index2.html', {'value': x})

        else:
            x = (-values[1] - math.sqrt(delta)) / (2 * values[0])
            x2 = (-values[1] + math.sqrt(delta)) / (2 * values[0])
            val = x, x2

            return render(request, 'index2.html', {'values': val})

    except Exception as error:

        return render(request, 'index2.html', {'error': error})

def pagina(request):

    if request.method == 'POST':

        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')

        a = int(a)
        b = int(b)
        c = int(c)


        vls = a, b, c

        return pagina2(request, vls)

    return render(request, 'index.html')
