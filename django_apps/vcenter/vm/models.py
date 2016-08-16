from __future__ import unicode_literals

from django.db import models

class Vm(models.Model):
    name = models.CharField(max_length=170,null=True)
    ip = models.CharField(max_length=30,null=True)
    uuid = models.CharField(max_length=60,null=True)

    def __unicode__(self):
        return self.name
class VmDetails(models.Model):
    vm = models.ForeignKey(Vm,on_delete=models.CASCADE)
    powerstate = models.CharField(max_length=10, null=True)
    maxcpuusage = models.CharField(max_length=20, null=True)
    maxmemoryusage = models.CharField(max_length=20, null=True)
    template = models.CharField(max_length=10, null=True)
    memorysizemb = models.IntegerField(null=True)
    numcpu = models.IntegerField(null=True)
    numethernetcards = models.IntegerField(null=True)
    numvirtualdisks = models.IntegerField(null=True)
    #instanceUuid = models.CharField(max_length=100, null=True)
    uuid = models.CharField(max_length=100, null=True)
    committed = models.CharField(max_length=120,null=True)
    uncommitted = models.CharField(max_length=120, null=True)
    overallcpuusage = models.IntegerField(null=True)
    overallcpudemand = models.IntegerField(null=True)
    guestmemoryusage = models.CharField(max_length=120,null=True)
    hostmemoryusage = models.CharField(max_length=120,null=True)
    guestheartbeatstatus = models.CharField(max_length=100, null=True)
    privatememory = models.CharField(max_length=120,null=True)
    consumedoverheadmemory = models.CharField(max_length=100, null=True)
    ftlatencystatus = models.CharField(max_length=100, null=True)
    host_ip = models.CharField(max_length=100, null=True)
    vcenter_date = models.DateField(null=True)
    createdate = models.DateField(null=True)

    def __unicode__(self):
        return self.host_ip

# Create your models here.
