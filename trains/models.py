from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


class Train(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Номер поїзда')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Час в дорозі')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  # , null=True, blank=True
                                  related_name='from_city_set',
                                  verbose_name='З якого міста')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE,
                                related_name='to_city_set',
                                verbose_name='В яке місто')

    def __str__(self):
        return f'Поїзд №{self.name} з {self.from_city} в {self.to_city}'

    class Meta:
        verbose_name = 'Поїзд'
        verbose_name_plural = 'Поїзди'
        ordering = ['travel_time']

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Змінити місто прибуття')
        qs = Train.objects.filter(
            from_city=self.from_city, to_city=self.to_city,
            travel_time=self.travel_time).exclude(pk=self.pk)
        # Train == self.__class__
        if qs.exists():
            raise ValidationError('Змініть час в дорозі')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class TrainTest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Номер поїзда')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  # , null=True, blank=True
                                  related_name='from_city',
                                  verbose_name='З якого міста')