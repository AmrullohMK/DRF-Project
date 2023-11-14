from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> QuerySet
    get -> retrieve -> Product Instance Detail View
    post-> create -> New Instance
    put -> Update
    patch -> Partial Update
    delete -> destroy
    '''
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
    ):
    
    '''
    CAN SELECT WITH METHODS TO CONTROL
    get -> list -> QuerySet
    get -> retrieve -> Product Instance Detail View
    '''
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    