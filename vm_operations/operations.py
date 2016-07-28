from vcenter_connect import vm_power_off
vm_name = raw_input("Enter a vm name: ")
print """
	1. power on
	2. power off
"""
option = raw_input("Enter an option:")
if option == '1':
	if vm_power_on(vm_name):
		print "power on"
	else:
		print "operation not performed"
elif option == '2':
	if vm_power_off(vm_name):
		print "power off"
	else:
		print "operation not performed"