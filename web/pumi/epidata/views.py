from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from epidata.models import Account, Epidata
from epidata.serializers import AccountSerializer, EpidataSerializer
from epidata.permissions import isAccountOwner

import json

class LoginView(views.APIView):
    parser_classes = (JSONParser,)
    def post(self, request, format = None):
        data = json.loads(request.body)

        username = data.get('username', None)
        password = data.get('password', None)
        account = authenticate(username = username, password = password)

        if account is not None:
            if account.is_active:
                login(request, account)
                serialized = AccountSerializer(account)
                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account is blocked.'
                }, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password not valid.'
            }, status = status.HTTP_401_UNAUTHORIZED)

class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return(permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status = status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with resolved data.'
        }, status = status.HTTP_400_BAD_REQUEST)

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
