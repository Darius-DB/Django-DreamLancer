from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from users.models import Profile
from .serializers import UserSerializer, ProfileSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer