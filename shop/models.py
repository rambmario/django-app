from django.db import models

# Create your models here.

class CategoryProd(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name = "categoryProd"
        verbose_name_plural = "categoriesProd"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    categories = models.ForeignKey(CategoryProd, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="shop", null=True, blank=True)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
