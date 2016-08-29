from sys import argv
import fo
if len(argv)==2:
	while True:
		print """
			1.Read
			2.Write
			3.Reset
			4.Exit
		"""
		file_name = argv[1]
		option = raw_input("Enter an option: ")
		if option == "1":
			fo.read_data(file_name)
		elif option == "2":
			fo.write_data(file_name)
		elif option == "3":
			fo.reset_file(file_name)
		elif option == "4":
			break
		else:
			print "Wrong option"
else:
	print """Usage: python app.py filename"""

     