from pyVim import connect
from pyVmomi import vim
import ssl
import pdb
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
si=connect.SmartConnect(host="",port=443,user="root",pwd="",sslContext=gcontext)
rootfolder = si.RetrieveContent().rootFolder
def get_vm_info(vm):
	pass
def get_all_hosts():
	count_host = 0
	for datacenter in rootfolder.childEntity:
		for host in datacenter.hostFolder.childEntity:
			host_obj = si.content.searchIndex.FindByIp(None,host.name,False)
			if host_obj:
				print "######Host information ############333"
				print "number of vms: ",len(host_obj.vm)
				print "ip address of host: ",host.name
				print "number of datastore:",len(host_obj.datastore)
				if hasattr(host_obj.summary,'numCpuCores'):
					print "number of cpu cores",host_obj.summary.numCpuCores
				if hasattr(host_obj.summary,'totalMemory'):
					print "Total memory in kb",host_obj.summary.totalMemory
				for vm in host_obj.vm:
					print "vm name:",vm.name
					print "power status:",vm.runtime.powerState
					print "maxCpuUsage: ",vm.runtime.maxCpuUsage
					print "maxMemoryUsage",vm.runtime.maxMemoryUsage
					print "Is template?",vm.config.template
					print "memorySizeMB:",vm.config.memorySizeMB
					print "numberof cpus:",vm.config.numCpu
					print "number of numEthernetCards:",vm.config.numEthernetCards
					print "number of virtual disks:",vm.config.numVirtualDisks
					print "instanceUuid:",vm.config.instanceUuid
					print "Bios uuid:",vm.config.uuid
					print "Commited:",vm.storage.committed
					print "Uncommited:",vm.storage.uncommitted
					print "unshared",vm.config.unshared
					print "overallCpuUsage:",vm.quickStats.overallCpuUsage
					print "overallCpuDemand:",vm.quickStats.overallCpuDemand
					print "guestMemoryUsage:",vm.guestMemoryUsage
					print "hostMemoryUsage:",vm.quickStats.hostMemoryUsage
					print "guestHeartbeatStatus:",vm.quickStats.guestHeartbeatStatus
					print "privateMemory:",vm.quickStats.privateMemory
					print "consumedOverheadMemory:",vm.quickStats.consumedOverheadMemory
					print "ftLatencyStatus:",vm.quickStats.ftLatencyStatus
				# summary = host_obj.summary
				# stats = summary.quickStats
				# hardware = host_obj.hardware
				# memorycapacityinmb = hardware
				# print "number of cpucores: "
				# count_datastore = 0
				# count_networkports = 0
				# count_host = count_host+1
				# if hasattr(host,'datastore'):
				# 	for datastore in host.datastore:
				# 		count_datastore = count_datastore + 1
				# 		print "###########datastore summary##############"
				# 		print datastore.summary
				# if hasattr(host,'network'):
				# 	for network in host.network:
				# 		count_networkports = count_networkports + 1
				# 		print "#########network#####################"
				# 		print network.summary
				# print "#############Summary##############"
				# if hasattr(host,'summary'):
				# 	print host.summary


