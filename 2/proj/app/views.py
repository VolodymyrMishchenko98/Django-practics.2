from django.shortcuts import render

def home(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def test(request):
    return render(request, 'app/test.html')

def contacts(request):
    return render(request, 'app/contacts.html')