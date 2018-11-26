from django.db import models

# Create your models here.
class Menu(models.Model):
    type = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=5, blank=True)
    numToppings = models.IntegerField(blank=True)
    cost = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        if type == "Pizza":
            return f"{size} {type} pizza with {numToppings} toppings (${cost})"
        else:
            return "test"
