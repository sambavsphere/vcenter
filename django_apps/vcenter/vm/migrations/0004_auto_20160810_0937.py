# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-10 09:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vm', '0003_auto_20160810_0736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vm',
            old_name='ip_address',
            new_name='ip',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='consumedOverheadMemory',
            new_name='consumedoverheadmemory',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='ftLatencyStatus',
            new_name='ftlatencystatus',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='guestHeartbeatStatus',
            new_name='guestheartbeatstatus',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='guestMemoryUsage',
            new_name='guestmemoryusage',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='hostMemoryUsage',
            new_name='hostmemoryusage',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='maxCpuUsage',
            new_name='maxcpuusage',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='maxMemoryUsage',
            new_name='maxmemoryusage',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='memorySizeMB',
            new_name='memorysizemb',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='numCpu',
            new_name='numVvirtualdisks',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='numEthernetCards',
            new_name='numcpu',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='numVirtualDisks',
            new_name='numethernetcards',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='overallCpuDemand',
            new_name='overallcpudemand',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='overallCpuUsage',
            new_name='overallcpuusage',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='powerState',
            new_name='powerstate',
        ),
        migrations.RenameField(
            model_name='vmdetails',
            old_name='privateMemory',
            new_name='privatememory',
        ),
    ]
