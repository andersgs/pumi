from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from epidata.models import Epidata
from epidata.serializers import EpidataSerializer

import json

def index(request):
    return HttpResponse("Hello, world. You're at the MGHA Pumi epidata index page.")

class EpidataViewSet(viewsets.ModelViewSet):
    lookup_field = 'patient_identifier'
    queryset = Epidata.objects.all() # modify this to show only from institution
    serializer_class = EpidataSerializer

    def get_permissions(self):
        ''' Make sure the user has persmission to create, view, or update data'''
        pass

    def create(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            Epidata.objects.create(**serializer.validated_data)

            return Response(serializer.validated_data, status = status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status = status.HTTP_400_BAD_REQUEST)
