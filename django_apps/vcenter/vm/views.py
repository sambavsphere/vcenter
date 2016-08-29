from django.shortcuts import render
from . models import Vm,VmDetails

def index(request):
	columns = [
'vcenter_date',
'powerstate',
 'maxcpuusage',
 'vm',
  'uncommitted',
 'memorysizemb',
 'committed',
 'consumedoverheadmemory',
 'numethernetcards',
  'template',
 'maxmemoryusage',
 'hostmemoryusage',
 'privatememory',
 'host_ip',
  'guestmemoryusage',
 'overallcpuusage',
 'overallcpudemand',
 'numvirtualdisks',
 'uuid',
 'numcpu',
 ]

	data = VmDetails.objects.all()
	return render(request,"vm/index.html",{'data':data,'columns':columns})

# Create your views here.
