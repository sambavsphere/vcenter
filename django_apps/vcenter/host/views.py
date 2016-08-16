from django.shortcuts import render
from . models import Host

def index(request):

	return render(request,"host/index.html",{'data':Host.objects.all()})

# Create your views here.
