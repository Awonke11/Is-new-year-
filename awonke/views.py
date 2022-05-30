from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, 'index.html')

def greet(request, name):
    return render(request, "greet.html", {
        "name": name
    })

