from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class SingletonModel(models.Model):
    class Meta:
        abstract = True


class Logo(SingletonModel):
    image = models.ImageField(upload_to='logos/')

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Logo, self).save(*args, **kwargs)

    def __str__(self):
        return f"Logo {self.pk}"

class StratContract1(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    file = models.FileField(
        blank=True, null=True, upload_to="documents/", default=False
    )
    desc = models.TextField()
    price = models.FloatField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class Contact1(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=120)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

