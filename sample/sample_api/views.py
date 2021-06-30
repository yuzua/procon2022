from django.shortcuts import render
from .models import Sample
from rest_framework import viewsets, filters
from .serializer import SampleSerializer

# Create your views here.

class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer