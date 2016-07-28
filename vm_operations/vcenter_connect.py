from pyVim import connect
from pyVmomi import vim
import ssl
import tasks
import pdb
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
si=connect.SmartConnect(host="",port=443,user="",pwd="",sslContext=gcontext)

def get_root():
    content = si.RetrieveContent()
    rootfolder = content.rootFolder
    print "Coneected to ",rootfolder.name , "Vcenter"
    return rootfolder

def select_vm_name(name):
    rootfolder = get_root()
    connected_vm = None
    for datacenter in rootfolder.childEntity:
        for vm in datacenter.vmFolder.childEntity:
            if vm.name == name:
                connected_vm = vm
                break
    if connected_vm:
        print "Connected to vm:",connected_vm.name
    return connected_vm
def vm_power_off(vm_name):
    vm = select_vm_name(vm_name)
    try:
        vm.PowerOff()
        return True
    except Exception as err:
        print err
    return False
def vm_power_on(vm_name):
    vm = select_vm_name(vm_name)
    try:
        vm.PowerOn()
        return True
    except Exception as err:
        print err
    return False

def add_disk(vm_name,disksize,disk_type):
    vm = select_vm_name(vm_name)
    spec = vim.vm.ConfigSpec()
    unit_number = 0
    dev_changes = []
    # get all disks on a VM, set unit_number to the next available
    for dev in vm.config.hardware.device:
        if hasattr(dev.backing, 'fileName'):
            unit_number = int(dev.unitNumber) + 1
            # unit_number 7 reserved for scsi controller
            if unit_number == 7:
                unit_number += 1
            if unit_number >= 16:
                print "we don't support this many disks"
                return
        if isinstance(dev, vim.vm.device.VirtualSCSIController):
            controller = dev
    if vm:
        print "Selected ",vm.name,"Virtual machine"
        disk_spec = vim.vm.device.VirtualDeviceSpec()

        new_disk_kb = int(disksize) * 1024 * 1024
        disk_spec = vim.vm.device.VirtualDeviceSpec()
        disk_spec.fileOperation = "create"
        disk_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        disk_spec.device = vim.vm.device.VirtualDisk()
        disk_spec.device.backing = \
            vim.vm.device.VirtualDisk.FlatVer2BackingInfo()
        if disk_type == 'thin':
            disk_spec.device.backing.thinProvisioned = True
        disk_spec.device.backing.diskMode = 'persistent'
        disk_spec.device.unitNumber = unit_number
        disk_spec.device.capacityInKB = new_disk_kb
        disk_spec.device.controllerKey = controller.key
        dev_changes.append(disk_spec)
        spec.deviceChange = dev_changes
        vm.ReconfigVM_Task(spec=spec)
        return True

    else:
        print "No vm provided with name:",vm_name
        return ""
    return ""
def get_all_disknumbers(vm_name):
    all_disk_numbers = []
    vm = select_vm_name(vm_name)
    for dev in vm.config.hardware.device:
        if hasattr(dev.backing, 'fileName'):
            all_disk_numbers.append(dev.unitNumber)
    return all_disk_numbers

def remove_disc(vm_name,disk_number):
    try:
        vm = select_vm_name(vm_name)
        hdd_prefix_label = 'Hard disk '
        hdd_label = hdd_prefix_label + str(disk_number)
        virtual_hdd_device = None
        for dev in vm.config.hardware.device:
            if isinstance(dev, vim.vm.device.VirtualDisk) \
                    and dev.deviceInfo.label == hdd_label:
                virtual_hdd_device = dev
        virtual_hdd_spec = vim.vm.device.VirtualDeviceSpec()
        virtual_hdd_spec.operation = \
            vim.vm.device.VirtualDeviceSpec.Operation.remove
        virtual_hdd_spec.device = virtual_hdd_device

        spec = vim.vm.ConfigSpec()
        spec.deviceChange = [virtual_hdd_spec]
        task = vm.ReconfigVM_Task(spec=spec)
        tasks.wait_for_tasks(si, [task])
        return True
    except Exception as err:
        print err
        return False
def disc_change_mode(vm_name,disk_number,mode):
    try:
        vm = select_vm_name(vm_name)
        hdd_prefix_label = 'Hard disk '
        hdd_label = hdd_prefix_label + str(disk_number)
        virtual_hdd_device = None
        for dev in vm.config.hardware.device:
            if isinstance(dev, vim.vm.device.VirtualDisk) \
                    and dev.deviceInfo.label == hdd_label:
                virtual_hdd_device = dev
        if not virtual_hdd_device:
            raise RuntimeError('Virtual {} could not be found.'.format(disk_label))
        virtual_hdd_spec = vim.vm.device.VirtualDeviceSpec()
        virtual_hdd_spec.operation = \
            vim.vm.device.VirtualDeviceSpec.Operation.edit
        virtual_hdd_spec.device = virtual_hdd_device
        virtual_hdd_spec.device.backing.diskMode = mode
        spec = vim.vm.ConfigSpec()
        spec.deviceChange = [virtual_hdd_spec]
        task = vm.ReconfigVM_Task(spec=spec)
        tasks.wait_for_tasks(si, [task])
        return True
    except Exception as err:
        print err
        return False

def update_virtual_disk_capacity(vm_name, disk_number, new_capacity_in_gb):
    """
    :param vm_obj: Virtual Machine Object
    :param disk_number: Disk Number to change
    :param new_capacity_in_gb: New Capacity in GB
    :param si: Service Instance
    :return: True if success
    """
    try:
        vm_obj = select_vm_name(vm_name)
        new_capacity_in_kb = gigabytes_to_kilobytes(long(new_capacity_in_gb))
        hard_disk_prefix_label = 'Hard disk '
        hard_disk_label = hard_disk_prefix_label + str(disk_number)
        virtual_disk_device = None
        for dev in vm_obj.config.hardware.device:
            if isinstance(dev, vim.vm.device.VirtualDisk) and dev.deviceInfo.label == hard_disk_label:
                virtual_disk_device = dev
        disk_exist = True if virtual_disk_device else False
        if disk_exist:
            old_capacity_in_gb = bytes_to_gigabytes(virtual_disk_device.capacityInBytes) \
                if virtual_disk_device.capacityInBytes else \
                kilobytes_to_gigabytes(virtual_disk_device.capacityInKB)
            if new_capacity_in_gb > old_capacity_in_gb:
                disk_spec = vim.vm.device.VirtualDeviceSpec()
                disk_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.edit
                disk_spec.device = vim.vm.device.VirtualDisk()
                disk_spec.device.key = virtual_disk_device.key
                disk_spec.device.backing = virtual_disk_device.backing
                disk_spec.device.backing.fileName = virtual_disk_device.backing.fileName
                disk_spec.device.backing.diskMode = virtual_disk_device.backing.diskMode
                disk_spec.device.controllerKey = virtual_disk_device.controllerKey
                disk_spec.device.unitNumber = virtual_disk_device.unitNumber
                disk_spec.device.capacityInKB = long(new_capacity_in_kb)
            elif new_capacity_in_gb == new_capacity_in_gb:
                return 'Disk capacity is the same. No change need to be done.'
            else:
                raise RuntimeError('Reducing Virtual Hard Disk Size is not supported at this time.')
        else:
            disks = list()
            for dev in vm_obj.config.hardware.device:
                if isinstance(dev, vim.vm.device.VirtualDisk):
                    disks.append(dev)
            next_unit_number = int(disks[-1].unitNumber) + 1
            current_controller_key = int(disks[-1].controllerKey)
            disk_spec = create_virtual_disk(new_capacity_in_kb, current_controller_key, next_unit_number, in_bytes=False)
        dev_changes = []
        dev_changes.append(disk_spec)
        spec = vim.vm.ConfigSpec()
        spec.deviceChange = dev_changes
        task = vm_obj.ReconfigVM_Task(spec=spec)
        tasks.wait_for_tasks(si, [task])
        return True
    except Exception as err:
        print err
        return False
