from django.db import models
# Add Our Product list
class Products(models.Model): 
    image = models.ImageField(upload_to='Myimage')
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
