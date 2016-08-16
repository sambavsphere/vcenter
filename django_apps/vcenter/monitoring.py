from time import sleep
import vcenter_moule
import pgd
import logging
logging.basicConfig(level=logging.DEBUG,filename="log.txt",format="%(asctime)s;%(levelname)s;%(message)s")
while True:
	try:
		count = 0
		host_info = vcenter_moule.get_all_host_info()
		logging.info(host_info)
		pgd.insert_host_details(host_info)
		while True:
			vm_info = vcenter_moule.get_all_vm_info()
			logging.info(vm_info)
			pgd.insert_vm_details(vm_info)
			count = count +1 
			if count%12 == 0:
				break
			sleep(300)
	except Exception as err:
		print err
		logging.exception(err)
	
