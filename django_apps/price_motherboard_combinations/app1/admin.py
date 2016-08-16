from django.contrib import admin

from . import models
admin.site.register(models.Cpu)
admin.site.register(models.Ram)
admin.site.register(models.Harddisk)
admin.site.register(models.Ssd)

# Register your models here.
