from __future__ import unicode_literals

from django.db import models

class Cpu(models.Model):
	model = models.CharField(max_length=12)
	price = models.FloatField()

	def __unicode__(self):
		return self.model+"->"+str(self.price)

class Ram(models.Model):
	size_gb = models.IntegerField()
	price = models.FloatField()

	def __unicode__(self):
		return str(self.size_gb)+"->"+self.price

class Harddisk(models.Model):
	size_gb = models.IntegerField()
	price = models.FloatField()

	def __unicode__(self):
		return str(self.size_gb)+"-> "+str(self.price)

class Ssd(models.Model):
	model = models.CharField(max_length=12)
	price = models.FloatField()

	def __unicode__(self):
		return self.model+"->"+str(self.price)

# Create your models here.
