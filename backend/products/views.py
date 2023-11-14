from rest_framework import generics, mixins #permissions, authentication
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.permissions import IsStaffEditorPermission
#from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    
    #lookup_field = 'pk Primary key'
    
class ProductListCreateAPIView(UserQuerySetMixin, generics.ListCreateAPIView, StaffEditorPermissionMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    def perform_create(self, serializer):
        #print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user= self.request.user,  content = content)
        # you can send Django signals here if you want as well
        
    # change this method into a mixin instead
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset()
    #     request = self.request
    #     #print(request.user)
    #     return qs.filter(user = request.user)
    
class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView,  generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            
class ProductDeleteAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    
    lookup_field = 'pk'
    
# class mixins to create custom class based views
# class ProductMixinView(mixins.CreateModelMixin,mixins.ListModelMixin , mixins.RetrieveModelMixin , generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'
#     permission_classes = [IsStaffEditorPermission, permissions.IsAdminUser]
#
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
        
#     def perform_create(self, serializer):
#         #print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = 'The mixin view is creating this!!! WOW'
#         serializer.save(content = content)
    
        
    
##--------------------------------------------------------------------------------------------------
# YOU CAN USE THIS GENERIC LIST VIEW AS WELL, BUT generics.ListCreateAPIView does that, and it dynamic to the request method (get,post)
# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer    
#     #lookup_field = 'pk Primary key'


# #ALL THREE POSTS COMBINED INTO 1 VIEW--------------------------------------------------------------------------------
# @api_view(['GET','POST',])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method
    
#     if method == 'GET':
#         if pk is not None:
#             # detail view
#             obj = get_object_or_404(Product, pk = pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)
            
#         # list view    
#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset, many=True).data
#         return Response(data)
    
#     if method == 'POST':
#         serializer = ProductSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content')
#             if content is None:
#                 content = title
#             serializer.save(content = content)
#             print(serializer.data)
#             return Response(serializer.data)
#         return Response({'invalid': 'not good data'}, status=400)
    
            

    