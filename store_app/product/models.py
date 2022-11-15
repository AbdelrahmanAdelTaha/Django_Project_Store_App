from django.db import models
from django.shortcuts import reverse

# Create your models here.
class ProductTable(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    no_of_item = models.IntegerField(default=0)

    def get_show_url(self):
        return reverse("products.show", kwargs={"id":self.id})

    def get_delete_url(self):
        return reverse("product.delete", kwargs={"id":self.id})

    def get_create_url(self):
        return reverse("product.create", kwargs={"id":self.id})

    def get_edit_url(self):
        return reverse("product.edit", kwargs={"pk": self.id})


