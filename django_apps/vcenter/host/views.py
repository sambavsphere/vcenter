from django.shortcuts import render
from . models import Host,HostDetails

def index(request):
	columns = ['host','numberofvms','memorysize','numberofdatastores','numcpucores',
	'overallcpuusage','overallstatus','numnics','hostmaxvirtualdiskcapacity','overallmemoryusage']
	data = HostDetails.objects.all()
	return render(request,"host/index.html",{'data':data,'columns':columns})

# Create your views here.
