from vcenter_connect import get_all_disknumbers,remove_disc
virtualmachine_name = raw_input("enter virtual machine name:")
all_disks_numbers = get_all_disknumbers(virtualmachine_name)
print "All disks number avaliable:"
print ",".join(map(str,all_disks_numbers))
selected_disk_number = int(raw_input("Selec a disk number:"))
if selected_disk_number in all_disks_numbers:
	if remove_disc(virtualmachine_name,selected_disk_number):
		print "Disc deleted"
	else:
		print "Something went wrong"

else:
	print "Please select proper disc number"




