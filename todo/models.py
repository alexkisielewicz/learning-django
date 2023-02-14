from django.db import models


# Create your models here.
# If we want functionality from one class inside another,
# we need to do inherit what we need, we inherit all basic django model here
class Item(models.Model):
    # null prevents from being empty, blank makes it required in forms
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
