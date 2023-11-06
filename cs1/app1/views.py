from django.shortcuts import render

# Create your views here.

def add(request):
    response = render(request, 'app1/set.html')
    response.set_cookie('name', 'brijesh')
    return response

def display(request):
    #nm = request.COOKIES['name']
    nm = request.COOKIES.get('name', "guest") # this get methoe have 2 points 1 is it return null if no cookies is found and we can alo add default
    return render(request, 'app1/display.html', {'name': nm})

def delete(request):
    response = render(request, 'app1/delete.html')
    response.delete_cookie('name')
    return response