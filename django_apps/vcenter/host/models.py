from __future__ import unicode_literals

from django.db import models

class Host(models.Model):
    name = models.CharField(max_length=120,null=True)
    ip = models.CharField(max_length=30,null=True)
    uuid = models.CharField(max_length=60,null=True)

    def __unicode__(self):
        return self.name

class HostDetails(models.Model):
    host = models.ForeignKey(Host,on_delete=models.CASCADE)
    numberofvms = models.CharField(max_length=100, null=True)
    #ipaddress = models.CharField(max_length=100, null=True)
    numberofdatastores = models.IntegerField(null=True)
    memorysize = models.CharField(max_length=100,null=True)
    numcpucores = models.IntegerField(null=True)
    numnics = models.IntegerField(null=True)
    cpumodel = models.CharField(max_length=100, null=True)
    cpumhz = models.CharField(max_length=100, null=True)
    numcpupkgs = models.IntegerField(null=True)
    numhbas = models.IntegerField(null=True)
    uuid = models.CharField(max_length=100, null=True)
    overallstatus = models.CharField(max_length=100, null=True)
    port = models.CharField(max_length=100, null=True)
    vmotionenabled = models.CharField(max_length=100, null=True)
    uptime = models.CharField(max_length=100, null=True)
    overallmemoryusage = models.CharField(max_length=100, null=True)
    overallcpuusage = models.CharField(max_length=100, null=True)
    boottime = models.CharField(max_length=100, null=True)
    connectionstate = models.CharField(max_length=100, null=True)
    dashoststate = models.CharField(max_length=100, null=True)
    hostmaxvirtualdiskcapacity = models.CharField(max_length=100, null=True)
    maxevcmodekey = models.CharField(max_length=100, null=True)
    managementserverip = models.CharField(max_length=100, null=True)
    currentevcmodekey = models.CharField(max_length=100, null=True)
    customvalue = models.CharField(max_length=100, null=True)
    vcenter_date = models.DateField(null=True)
    createdate = models.DateField(null=True)


# Create your models here.
