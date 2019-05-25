from django.db import models


# Create your models here.
class Execution(models.Model):
    time = models.DateTimeField('Time of script finished')
    amount = models.IntegerField('Amount of devices found')
    execution = models.FloatField('NMap execution time')
    from_index = models.BooleanField("If from index template?", default=False)

    class Meta:
        verbose_name = 'Data from KenCan execution'
        verbose_name_plural = 'Data from KenCan execution'

    def __str__(self):
        return str(self.time)


class Device(models.Model):
    script = models.ForeignKey(Execution, related_name='devices', on_delete=models.CASCADE)
    ip = models.CharField('IPv4 Address', max_length=255)
    domain = models.CharField('Domain', max_length=255)

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

    def __str__(self):
        return self.ip
