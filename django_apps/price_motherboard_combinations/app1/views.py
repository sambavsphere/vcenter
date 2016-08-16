from django.shortcuts import render,render_to_response
from models import Cpu, Harddisk, Ram, Ssd
def get_combinations(l):
	comb=[]
	le = len(l)
	i=0
	while i<le:
	    j=i
	    while j<le:
	        comb.append((l[i],l[j]))
	        j=j+1
	    i=i+1
	return comb
def calc(request):
	cpus = Cpu.objects.all()
	harddisks = Harddisk.objects.all()
	rams = Ram.objects.all()
	ssds = Ssd.objects.all()
	twoslots_harddisks=get_combinations(harddisks)
	twoslots_rams=get_combinations(rams)
	twoslots_ssds=get_combinations(ssds)

	result = []
	for cpu in cpus:
		for ram in rams:
			for harddisk in harddisks:
				for ssd in ssds:
					total = cpu.price+ram.price+harddisk.price+ssd.price
					result.append({
						'cpu':cpu.model,
						'ram':ram.size_gb,
						'hd':harddisk.size_gb,
						'ssd':ssd.model,
						'total':total
						})
	for cpu in cpus:
		for twoslots_ram in twoslots_rams:
			for twoslots_harddisk in twoslots_harddisks:
				for twoslots_ssd in twoslots_ssds:
					total = twoslots_ssd[0].price+twoslots_ssd[1].price\
					+twoslots_harddisk[0].price+twoslots_harddisk[1].price\
					+twoslots_ssd[0].price+twoslots_ssd[1].price
					result.append({
						'cpu':cpu.model,
						'ram':str(twoslots_ram[0].size_gb)+","+str(twoslots_ram[1].size_gb),
						'hd':str(twoslots_harddisk[0].size_gb)+","+str(twoslots_harddisk[1].size_gb),
						'ssd':str(twoslots_ssd[0].model)+","+str(twoslots_ssd[1].model),
						'total':total
						})


	return render_to_response('index.html',{'result':result})


# Create your views here.
