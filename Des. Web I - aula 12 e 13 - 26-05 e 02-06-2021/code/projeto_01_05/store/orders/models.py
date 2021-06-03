from django.db import models
from model_utils.models import TimeStampedModel
from products.models import Product
from users.models import User
# Create your models here.

class Order(TimeStampedModel):
    user = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE)
    name = models.CharField("Nome Completo", max_length=250)
    postal_code = models.CharField("CEP", max_length=9)
    address = models.CharField("Endereço", max_length=250)

    def __str__(self):
        return str(self.id)

    @property
    def get_total_price(self):
        total_cost = sum(item.get_cost for item in self.items.all())
        return total_cost

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cost(self):
        return self.product.price * self.quantity