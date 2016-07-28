# using Tkinter's Optionmenu() as a combobox
try:
    # Python2
    import vcenter_performance_monitoring as vpm
    import Tkinter as tk
    import tkMessageBox
    si = vpm.connectvcenter()
except ImportError:
    # Python3
    import tkinter as tk
def select():
    matrick = var.get()
    vm = var2.get()
    res=vpm.get_summary(si,vm,matrick)
    tkMessageBox.showinfo( "", res)
    
root = tk.Tk()
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (330, 80, 200, 150))
root.title("Vcenter performance monitoring")
var = tk.StringVar(root)
var2 = tk.StringVar(root)
# initial value
vms = vpm.get_all_vms(si)
var.set('summary')
var2.set(vms[0])
metricks = ['summary','powerState','quickStats','overallStatus','guest','config','storage']
matrick_dropdown = tk.OptionMenu(root, var, *metricks)
matrick_dropdown.pack(side='left', padx=10, pady=10)
vms_dropdown = tk.OptionMenu(root,var2,*vms)
vms_dropdown.pack()
button = tk.Button(root, text="Pollit", command=select)
button.pack(side='left', padx=20, pady=10)
root.mainloop()
