from django.shortcuts import render

def home(request):
    # Your view logic goes here
    return render(request, 'home.html')
