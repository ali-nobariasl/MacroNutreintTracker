from django.shortcuts import render

from  myapp.models import Food



def index(request):
    foods  = Food.objects.all()
    return render(request, 'myapp/index.html', {'foods': foods})