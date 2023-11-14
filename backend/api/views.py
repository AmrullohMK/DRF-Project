#from django.http import JsonResponse, HttpResponse
#import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request,*args, **kwargs):
    '''DRF API VIEW'''
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


## GET RESPONSE/REQUEST ##-------------------------------------------------------
# @api_view(["GET"])
# def api_home(request,*args, **kwargs):
#     '''DRF API VIEW'''
#     instance = Product.objects.all().order_by('?').first()
#     data = {}
    
#     if instance:
#         #data = model_to_dict(model_data, fields= ['id','price','title','sale_price'])
#         data = ProductSerializer(instance).data
#     return Response(data)   

    ## TEST GARBAGE, DONT PAY ATTENTION, THESE ARE PERSONAL NOTES ##------------------------------------------
    # # this request parameter is a django request class:
    # #request -> HttpRequest -> Django : GOT NOTHING TO DO WITH requests.
    # #request.body is usualy the json byte string
    
    # body = request.body 
    # print(request.GET)
    # print(request.POST)
    # data = {}
    # try:
    #     data = json.loads(body) # turns the json into a python dict
    # except:
    #     pass
    
    # print(data)
    
    # #data['headers'] = request.headers --> it cannot turn the dictionary headers back into json / not json serialable
    # data['headers'] = dict(request.headers)
    # data['params'] = dict(request.GET)
    # data['content_type'] = request.content_type # adding a new dict variable that represents the content_type of our request
    
    # return JsonResponse(data)