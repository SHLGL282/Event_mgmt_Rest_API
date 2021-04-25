from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from event_app.models import EventMaster, CategoryMaster
from rest_framework import viewsets, permissions
from event_app.serializers import UserSerializer, EventMasterSerializer, CategoryMasterSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventMasterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = EventMaster.objects.all().order_by('-time')
    #queryset = EventMaster.objects.filter(event_name).order_by('-time')
    serializer_class = EventMasterSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryMasterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CategoryMaster.objects.all()
    serializer_class = CategoryMasterSerializer
    permission_classes = [permissions.IsAuthenticated]

# class EventMasterEndViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
