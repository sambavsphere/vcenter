from Tkinter import Text, Tk, END, mainloop
from os.path import isfile


def read_data(file_name):
    print "read operation..........."
    if isfile(file_name):
        f = open(file_name)
    else:
        f = open(file_name+"_backup")
    print "Getting the data from: ", f.name
    data = f.readlines()
    print data


def write_data(file_name):
    f=""
    data = ""
    if isfile(file_name):
        f = open(file_name, 'a+')
        f_b = open(file_name+"_backup", 'a+')
    else:
        f=open(file_name+"_backup","a+")
        f_b = open(file_name+"_buffer", 'a+')


    def keyup_write_twofiles(e):
        c = e.char
        f.write(c)
        f_b.write(c)
        f.flush()
        print "Written {0} in to {1}".format(c,f.name)
        f_b.flush()
        print "Written {0} in to {1}".format(c,f_b.name)
    def keyup_write_onefile(e):
        c=e.char
        f_b.write(c)
        f_b.flush()
        print "Written {0} in to {1}".format(c,f_b.name)

    data = f.read()
    root = Tk()
    T = Text(root, height=100, width=100)
    T.pack()
    T.insert(END, data)
    if isfile(file_name):
        T.bind("<KeyRelease>", keyup_write_twofiles)
    else:
        T.bind("<KeyRelease>", keyup_write_onefile)
    mainloop()
def reset_file(file_name):
    backup_file = file_name+"_backup"
    buffer_file = file_name+"_buffer"
    if isfile(file_name):
        return "Reset Not required"
    elif isfile(backup_file):
        f_backup=open(backup_file,'a')
        if isfile(buffer_file):
            f_buffer=open(buffer_file)
            
            buffer_data = f_buffer.read()
            f_backup.write(buffer_data)
            res = "Reset done successfully from {0} -> {1}".format(f_buffer.name,f_backup.name)
            f_buffer.close()
            f_backup.close()
            return res
        else:
            f_backup.close()
            return "Reset operation failed: Buffer file not found!!"

