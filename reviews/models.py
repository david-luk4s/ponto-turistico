from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField('Comentário', null=True, blank=True)
    note = models.DecimalField(max_digits=3, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' : ' + self.review

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
