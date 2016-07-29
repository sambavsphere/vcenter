'''
Program to monitor the vcenter
1. Number of hosts and names
2. Get all vms in each hosts
3. Find the below matrics for every vm
    a. CPU utilization number of cores
    b. RAM utilization
    c. Storage
    d. Nic utilization
'''
from pyVim import connect
import ssl
from pyVmomi import vim
import pdb
class VcenterTest:
    si=None;
    def __init__(self):
        if(self.si!=None):
            print "making connectionnnnnnnn"
            gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            self.si=connect.SmartConnect(host="",port=443,user="root",pwd="",sslContext=gcontext)
        
    def get_root(self):
        content = self.si.RetrieveContent()
        rootfolder = content.rootFolder
        print "Coneected to ",rootfolder.name , "Vcenter"
        return rootfolder

    def select_vm_name(self,name):
        rootfolder = self.get_root()
        connected_vm = None
        for datacenter in rootfolder.childEntity:
            for vm in datacenter.vmFolder.childEntity:
                if vm.name == name:
                    connected_vm = vm
                    break
        return connected_vm


    def get_all_vms(self):
        list_vms = []
        for datacenter in self.si.RetrieveContent().rootFolder.childEntity:
            for vm in datacenter.vmFolder.childEntity:
                #pdb.set_trace()
                list_vms.append(vm.summary.config.name)
        return list_vms

    def get_summary(self,vm_name,option):
        vm = self.select_vm_name(vm_name)
        if option == 'summary':
            result = vm.summary
        elif option == 'config':
            result = vm.summary.config
        elif option == 'storage':
            result = vm.summary.storage
        elif option == 'quickStats':
            result = vm.summary.quickStats
        elif option == 'guest':
            result = vm.summary.guest
        elif option == 'powerState':
            result = vm.summary.runtime.powerState
        elif option == 'overallStatus':
            result = vm.summary.overallStatus
        else:
            result = vm.summary
        return str(result)


