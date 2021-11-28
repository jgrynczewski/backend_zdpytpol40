from django.db import models

# one-to-one relation
class Country(models.Model):
    name = models.CharField(max_length=128)


class Capital(models.Model):
    name = models.CharField(max_length=128)
    country = models.OneToOneField(
        'country',
        on_delete=models.CASCADE,
    )


# one-to-many relation
class Language(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class Framework(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey(
        'language',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.name}"


# many-to-many relation
class Movie(models.Model):
    name = models.CharField(max_length=256)


class Character(models.Model):
    name = models.CharField(max_length=128)
    movies = models.ManyToManyField(Movie)


class Car(models.Model):
    year = models.IntegerField()
    model = models.CharField(max_length=128)


class CarAdvertisement(models.Model):
    title = models.CharField(max_length=256)
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    car = models.ForeignKey(
        'car',
        on_delete=models.CASCADE
    )
