from django.db import models


class HydroponicSystem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    owner = models.ForeignKey(
        'auth.User', related_name='hydroponic_systems', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def last_10_measurements(self):
        return self.measurements.order_by('-created_at')[:10]


class Measurement(models.Model):
    hydroponic_system = models.ForeignKey(
        HydroponicSystem, related_name='measurements', on_delete=models.CASCADE)
    ph = models.FloatField()
    water_temp = models.FloatField()
    tds = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.hydroponic_system.name} - {self.created_at}'
