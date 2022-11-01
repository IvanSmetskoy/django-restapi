from email import header
#import json
from django.forms.models import model_to_dict
#from django.http import JsonResponse, HttpResponse
from products.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):

    """DRF API VIEW"""

    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:

        data = ProductSerializer(instance).data
    return Response(data)
