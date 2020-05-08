from django.db import models


class Location(models.Model):
    line_one = models.CharField('Linha 1', max_length=150)
    line_two = models.CharField('Linha 2', max_length=150, null=True, blank=True)
    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado', max_length=50)
    nation = models.CharField('País', max_length=50)
    lat = models.IntegerField('Latitude', null=True, blank=True)
    long = models.IntegerField('Longitude', null=True, blank=True)

    def __str__(self):
        return self.line_one

    class Meta:
        verbose_name = 'Localização'
        verbose_name_plural = 'Localizações'


