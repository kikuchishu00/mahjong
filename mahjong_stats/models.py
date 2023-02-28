from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass


class Stats(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(
        blank=False,
        null=False,
        verbose_name="日付",
    )
    counts = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="打荘回数",
    )
    points = models.FloatField(
        blank=False,
        null=False,
        verbose_name="ポイント",
    )
    first = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="一着回数",
    )
    second = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="二着回数",
    )
    third = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="三着回数",
    )
    fourth = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="四着回数",
    )



