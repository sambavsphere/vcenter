from vcenter_connect import update_virtual_disk_capacity, get_all_disknumbers
virtualmachine_name = 'Nexii2'  #raw_input("enter virtual machine name:")
all_disks_numbers = get_all_disknumbers(virtualmachine_name)
print "All disks number avaliable:"
print ",".join(map(str,all_disks_numbers))
selected_disk_number = int(raw_input("Selec a disk number:"))
disk_size = raw_input("Enter Disk size:")
if selected_disk_number in all_disks_numbers:
	if update_virtual_disk_capacity(virtualmachine_name,selected_disk_number,disk_size):
		print "Disc mode is changed"
	else:
		print "Something went wrong"

else:
	print "Please select proper disc number"




