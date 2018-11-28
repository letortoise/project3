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

    # Define the ordering for the menu items
    class Meta:
        ordering = ["type", "size", "numToppings"]

    def __str__(self):
        if self.type == "Regular Pizza" or "Sicilian Pizza":
            return f"{self.numToppings} topping {self.get_size_display()} {self.get_type_display()}"
        else:
            return f"{self.get_size_display()} {self.name} {self.get_type_display()}"

class Extra(models.Model):

    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):

    username = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.pk} - {self.username}"

class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    extras = models.ManyToManyField(Extra, blank=True)

    def __str__(self):
        return f"({self.order}) {self.item} with {self.extras}"
