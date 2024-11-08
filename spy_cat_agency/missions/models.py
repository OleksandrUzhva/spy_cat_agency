from django.db import models
from cats.models import Cat

class Mission(models.Model):
    cat = models.OneToOneField(Cat, null=True, blank=True, on_delete=models.SET_NULL)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Mission for {self.cat.name if self.cat else 'Unassigned'}"

class Target(models.Model):
    mission = models.ForeignKey(Mission, related_name="targets", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Target {self.name} in {self.country}"