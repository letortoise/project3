from django.db import models

# Create your models here.
class MenuItem(models.Model):

    ITEM_TYPES = (
        ('RP', 'Regular Pizza'),
        ('SP', 'Sicilian Pizza'),
        ('SU', 'Sub'),
        ('PA', 'Pasta'),
        ('SA', 'Salad'),
        ('DP', 'Dinner Platter')
    )
    type = models.CharField(max_length=64, choices=ITEM_TYPES)

    name = models.CharField(max_length=64, blank=True)

    ITEM_SIZES = (
        ('SM', 'Small'),
        ('LG', 'Large'),
        ('ONE', 'One Size')
    )
    size = models.CharField(max_length=12, choices=ITEM_SIZES)

    numToppings = models.IntegerField(blank=True)

    cost = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        if self.type == "Regular Pizza" or "Sicilian Pizza":
            return f"{self.size} {self.type} with {self.numToppings} toppings (${self.cost})"
        else:
            return f"{self.size} {self.name} {self.type} ({self.cost})"
