from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
    if request.session['count'] == None:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    request.session['response'] = get_random_string(length=32)
    return render(request, 'randomApp/index.html')
def process(request):
    return redirect('/', request)