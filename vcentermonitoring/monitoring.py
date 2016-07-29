from time import sleep
from vcenter import get_all_host_info, get_all_vm_info
from sqlit import insert_host_info, insert_vm_info
import logging
logging.basicConfig(level=logging.DEBUG,filename="log.txt",format="%(asctime)s;%(levelname)s;%(message)s")
while True:
	try:
		count = 0
		host_info = get_all_host_info()
		logging.info(host_info)
		insert_host_info(host_info)
		while True:
			vm_info = get_all_vm_info()
			logging.info(vm_info)
			insert_vm_info(vm_info)
			count = count +1 
			if count%12 == 0:
				break
			sleep(300)
	except Exception as err:
		logging.exception(err)