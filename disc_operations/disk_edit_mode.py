from vcenter_connect import get_all_disknumbers,disc_change_mode
virtualmachine_name = 'Nexii2'  #raw_input("enter virtual machine name:")
all_disks_numbers = get_all_disknumbers(virtualmachine_name)
print "All disks number avaliable:"
print ",".join(map(str,all_disks_numbers))
selected_disk_number = int(raw_input("Selec a disk number:"))
all_modes = ['independent_persistent',
                                 'persistent',
                                 'independent_nonpersistent',
                                 'nonpersistent',
                                 'undoable',
                                 'append']
print ",".join(all_modes)
selected_mode = raw_input("Select a mode:")

if selected_disk_number in all_disks_numbers and selected_mode in all_modes:
	if disc_change_mode(virtualmachine_name,selected_disk_number,selected_mode):
		print "Disc mode is changed"
	else:
		print "Something went wrong"

else:
	print "Please select proper disc number"




