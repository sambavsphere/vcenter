from django.shortcuts import render
from . models import Host,HostDetails

def index(request):
	columns = HostDetails._meta.get_all_field_names()
	data = HostDetails.objects.all()
	return render(request,"host/index.html",{'data':data,'columns':columns})

# Create your views here.
