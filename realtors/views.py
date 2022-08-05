from django.shortcuts import render
from django.http import JsonResponse
from .models import Realtor
from .serializers import RealtorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def realtor_list(request):

    if request.method == 'GET':
        realtors = Realtor.objects.all()
        serializer = RealtorSerializer(realtors, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializers = RealtorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# Create your views here.
