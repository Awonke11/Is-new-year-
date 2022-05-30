from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def main(request):
    current_date = datetime.datetime.now()
    condition = False
    if current_date.month == 1 and current_date.day == 1:
        condition = True
    return render(request, 'new/index.html', {
        "newyear": condition 
    })
    