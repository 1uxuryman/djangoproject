from django.db import models

# Create your models here.


class Film(models.Model):
    title = models.CharField(max_length=100)
    producer =models.CharField(max_length=50)
    rate = models.PositiveIntegerField(default=0,verbose_name="Rating")
    duration = models.DurationField(verbose_name="Durex")
    image = models.ImageField(upload_to="", null=True)


    def __str__(self):
        return str(self.title)


class Rewiev(models.Model):
    id_pole = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, on_delete = models.CASCADE)
    text = models.TextField(max_length=500, verbose_name="Текст")

    def __str__(self):
        return str(self.id_pole)


