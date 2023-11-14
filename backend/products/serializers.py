from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from .validators import validate_title_no_hello, unique_product_title
from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    #my_user_data = serializers.SerializerMethodField(read_only = True)
    #discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )
    title = serializers.CharField(validators = [validate_title_no_hello, unique_product_title])
    #name = serializers.CharField(source = 'title', read_only=True)
    #email = serializers.EmailField(write_only=True)
    #user = serializers.CharField(source = 'user.username',read_only=True )
    owner = UserPublicSerializer(source = 'user',read_only = True)
    class Meta:
        model = Product
        fields = ['owner',
                  'url',
                  'edit_url',   
                  'pk', 
                  'title',
                  #'name',
                  'content',
                  'price',
                  'sale_price',
                  #'discount',
                  'public',
                  ]
        
    def get_edit_url(self, obj):
        # when working with views, you can do self.request, but with model methods, its self.context.get('request')
        request = self.context.get('request') #self.request
        if request is None:
            return None
        return reverse('product-edit',kwargs = {'pk': obj.pk}, request=request)
    
    
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} is already a product name.')
    #     return value
    
    ##ARBITRARY METHODS TO USE DATA NOT CONTAINED IN MODEL
    # def create(self, validated_data):
    #     obj =  super().create(validated_data)
    #     #email = validated_data.pop('email')
    #     #print(email , obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title')
    #     return instance
    
    # def get_my_user_data(self, obj):
    #     return {
    #         'username': obj.user.username
    #     }
    
    
    # def get_discount(self, obj):
    #     try:
    #         return obj.get_discount()
    #     except:
    #         return None