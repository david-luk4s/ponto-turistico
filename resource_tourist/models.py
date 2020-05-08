from django.db import models


class ResourceTourist(models.Model):
    name = models.CharField('Nome', max_length=150)
    description = models.TextField()
    time_func = models.CharField('Horário de Funcionamento', max_length=200)
    date_register = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='resource_tourist', null=True, blank=True)

    class Meta:
        verbose_name = 'Recurso Turistíco'
        verbose_name_plural = 'Recursos Turistícos'

    def __str__(self):
        return self.name + self.time_func