from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{boldmessage}} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Return a rendered response
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Nik Harith'}

    # Return a rendered response
    return render(request, 'rango/about.html', context=context_dict)