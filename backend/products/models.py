from django.db import models
from django.conf import settings
from django.db.models.query import QuerySet
from django.db.models import Q
import random
# Create your models here.

User = settings.AUTH_USER_MODEL # auth.User

TAGS_MODEL_VALUES = ['electronics', 'cars', 'boats', 'movies', 'cameras' ]

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public = True)
    
    def search(self, query, user = None):
        lookup = Q(title__icontains = query) | Q(content__icontains = query)
        qs = self.is_public().filter(lookup)
        if User is not None:
            qs2 = self.filter(user = user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs # the queryset returns the public products of the search and the private products if the user is defined


# used to get the query set of any model that could be in the API, not only products
class ProductManager(models.Manager):
    
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using = self._db) # makes so the model is the parameter put in , using the its self as a db
    
    
    def search(self, query, user=None):
        return self.get_queryset().search(query, user = user)
    


class Product(models.Model):
    user = models.ForeignKey(User,default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2,default=99.99)
    public = models.BooleanField(default=True)
    #objects = ProductManager()
    
    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]
    
    def is_public(self):
        return self.public
    
    def __str__(self):
        return f'{self.title}'
    
    @property
    def sale_price(self) -> bool:
        return '%.2f' %(float(self.price)* 0.8)
    
    def get_discount(self):
        return '%.2f' %(float(self.price)* 0.5)
    