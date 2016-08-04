from pyVim import connect
from pyVmomi import vim
import ssl
import pdb
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
si=connect.SmartConnect(host="",port=443,user="root",pwd="",sslContext=gcontext)
rootfolder = si.RetrieveContent().rootFolder


def get_all_vm_info():
    all_vm_info = []
    for datacenter in rootfolder.childEntity:
        for vm in datacenter.vmFolder.childEntity:
            if isinstance(vm,vim.VirtualMachine):
                current_vm_info=""
                current_vm_info = get_vminfo(vm)
                if current_vm_info:
                    all_vm_info.append(current_vm_info)
    return all_vm_info


def get_vminfo(vm):
    vminfo={}
    vminfo['name'] = vm.name
    
    summary = vm.summary
    vminfo['powerState'] = summary.runtime.powerState
    vminfo['maxCpuUsage'] = summary.runtime.maxCpuUsage
    vminfo['maxMemoryUsage'] = summary.runtime.maxMemoryUsage
    vminfo['template'] = summary.config.template
    vminfo['memorySizeMB'] = summary.config.memorySizeMB
    vminfo['numCpu'] = summary.config.numCpu
    vminfo['numEthernetCards'] = summary.config.numEthernetCards
    vminfo['numVirtualDisks'] = summary.config.numVirtualDisks
    vminfo['instanceUuid'] = summary.config.instanceUuid
    vminfo['uuid'] = summary.config.uuid
    vminfo['committed'] = summary.storage.committed
    vminfo['uncommitted'] = summary.storage.uncommitted
    vminfo['overallCpuUsage'] = summary.quickStats.overallCpuUsage
    vminfo['overallCpuDemand'] = summary.quickStats.overallCpuDemand
    vminfo['guestMemoryUsage'] = summary.quickStats.guestMemoryUsage
    vminfo['hostMemoryUsage'] = summary.quickStats.hostMemoryUsage
    vminfo['guestHeartbeatStatus'] = summary.quickStats.guestHeartbeatStatus
    vminfo['privateMemory'] = summary.quickStats.privateMemory
    vminfo['consumedOverheadMemory'] = summary.quickStats.consumedOverheadMemory
    vminfo['ftLatencyStatus'] = summary.quickStats.ftLatencyStatus
    vminfo['host_ip'] = summary.runtime.host.name
    vminfo['vcenter_date_time'] = si.CurrentTime()
    return vminfo

    
def get_all_host_info():
    count_host = 0
    all_host_info = []
    for datacenter in rootfolder.childEntity:
        for host in datacenter.hostFolder.childEntity:
            current_host_info = ""
            current_host_info = get_host_info(host)
            if current_host_info:
                all_host_info.append(current_host_info)
    return all_host_info


def get_host_info(host):
    host_obj = si.content.searchIndex.FindByIp(None,host.name,False)
    host_info = {}
    if host_obj:
        host_info['numberofvms'] = len(host_obj.vm)
        host_info['ipaddress'] = host.name
        summary = host_obj.summary
        hardware = summary.hardware
        stats = summary.quickStats
        config = summary.config
        runtime = summary.runtime
        host_info['numberofdatastores'] = len(host_obj.datastore)
        host_info['memorySize'] = hardware.memorySize 
        host_info['numCpuCores'] = hardware.numCpuCores
        host_info['numNics'] = hardware.numNics
        host_info['cpuModel'] = hardware.cpuModel
        host_info['cpuMhz'] = hardware.cpuMhz
        host_info['numCpuPkgs'] = hardware.numCpuPkgs
        host_info['numHBAs'] = hardware.numHBAs
        host_info['uuid'] = hardware.uuid
        host_info['overallStatus'] = summary.overallStatus
        host_info['port'] = config.port
        host_info['vmotionEnabled'] = config.vmotionEnabled
        host_info['uptime'] = stats.uptime
        host_info['overallMemoryUsage'] = stats.overallMemoryUsage
        host_info['overallCpuUsage'] = stats.overallCpuUsage
        host_info['bootTime'] = runtime.bootTime
        host_info['connectionState'] = runtime.connectionState
        host_info['dasHostState'] = runtime.dasHostState
        host_info['hostMaxVirtualDiskCapacity'] = runtime.hostMaxVirtualDiskCapacity
        host_info['maxEVCModeKey'] = summary.maxEVCModeKey
        host_info['managementServerIp'] = summary.managementServerIp
        host_info['currentEVCModeKey'] = summary.currentEVCModeKey
        host_info['customValue'] = summary.customValue
        host_info['vcenter_date_time'] = si.CurrentTime()
        

    return host_info
                


