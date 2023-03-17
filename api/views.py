from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reading
from .serializers import ReadingSerializer

@api_view(['GET', 'POST'])
def create_reading(request):
    if request.method == 'GET':
        create_reading = Reading.objects.all()
        serializer = ReadingSerializer(readings, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
    serializer = ReadingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

