from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=50)
    years_of_experience = models.IntegerField()
    breed = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name