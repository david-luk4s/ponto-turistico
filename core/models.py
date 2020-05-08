from django.db import models

#add imports models resource_tourist
from resource_tourist.models import ResourceTourist
from comment.models import Comment
from reviews.models import Review
from location.models import Location


class TouristPoint(models.Model):
    name = models.CharField('Nome', max_length=150)
    description = models.TextField('Descrição')
    approved = models.BooleanField('Aprovado', default=False)
    date_register = models.DateField(auto_now_add=True)
    resource_tourists = models.ManyToManyField(ResourceTourist, blank=True)
    comments = models.ManyToManyField(Comment, blank=True)
    review = models.ManyToManyField(Review, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='tourist_point', null=True, blank=True)

    def complet_description_two(self):
        return self.name + ' - ' + self.description

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ponto Turistico'
        verbose_name_plural = 'Pontos Turisticos'
