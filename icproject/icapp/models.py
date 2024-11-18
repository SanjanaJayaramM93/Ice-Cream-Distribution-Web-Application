from django.db import models


# Create your models here.
class Store(models.Model):
    store_name = models.CharField(max_length=100)
    store_location = models.CharField(max_length=100)
    store_email = models.EmailField(max_length = 254)
    def __str__(self):
        return self.store_name
class Tub(models.Model):
    is_choices = [(False, 'No'), (True, 'Yes')]
    tub_flavour = models.CharField(max_length=255)
    tub_size = models.FloatField()
    tub_vegan = models.BooleanField(verbose_name ="Vegan", default=False,choices=is_choices)                
    tub_gluten = models.BooleanField(verbose_name ="Gluten free", default=False,choices=is_choices)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    tub_image = models.ImageField(upload_to='tubs')
    def __str__(self):
        return self.tub_flavour