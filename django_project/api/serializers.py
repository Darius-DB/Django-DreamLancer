from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'date_joined']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    model = Profile
    fields = ['id', 'image', 'user_id', 'abilities_1', 'abilities_2', 'abilities_3', 'abilities_4', 'domain',
              'first_name', 'last_name', 'github_info', 'linkedin_info', 'years_of_experience', 'description']
