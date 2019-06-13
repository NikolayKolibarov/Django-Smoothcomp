from django.db import models

# Create your models here.

class Competition(models.Model):
    # auth = models.ManyToManyField(User)
    title = models.CharField(max_length=30)
    description = models.TextField()
    thumbnail = models.FileField(default='no-image.png')
    location = models.CharField(max_length=30)
    date = models.DateField()

    def __str__(self):
        return "%s the place" % self.title


class CompetitionCategory(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return "%s the place" % self.name
