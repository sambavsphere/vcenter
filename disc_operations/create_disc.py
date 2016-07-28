from vcenter_connect import add_disk
virtualmachine_name = raw_input("enter virtual machine name:")
disk_size = raw_input("Enter Disc size in GB:")
disk_type = raw_input("Enter Disc type:")
if add_disk(virtualmachine_name,disk_size,disk_type):
	print "Disc created"
else:
	print "Something went wrong"


