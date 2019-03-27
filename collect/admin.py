from django.contrib import admin

# Register your models here.
from collect.models import Device, Execution


@admin.register(Execution)
class ExecutionAdmin(admin.ModelAdmin):
    list_display = ('time', 'amount', 'execution')
    search_fields = ('execution',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('ip', 'domain', 'script')
    search_fields = ('ip',)
