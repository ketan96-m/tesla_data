from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from temperature.models import Data
from temperature.serializers import DataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utility import parse_data_string

# Create your views here.


@api_view(['POST'])
def postData(request):
    serializer = DataSerializer(data=request.data)
    errors = Data()
    if serializer.is_valid():
        result = parse_data_string(serializer.validated_data['data'])
        if result is not None:
            return Response(result, status=201)
        else:
            serializer.save()
    return Response({
                "error": "bad request"
            }, status=400)
    


@api_view(['GET','DELETE'])
def get_delete_Data(request):
    if request.method=='GET':
        temperature = Data.objects.all().values_list('data',flat=True)
        # serializer = DataSerializer(temperature, many=True)
        return Response({'errors':temperature})
    elif request.method=='DELETE':
        errors = Data.objects.all()
        errors.delete()
        return Response({'errors':Data.objects.all().values_list('data', flat=True)})

def home_redirect(request):
    response = HttpResponse(status=302)
    response['Location'] = '/temp/'
    return response