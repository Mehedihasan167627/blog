from rest_framework import serializers
from .models import User 
from django.contrib.auth.hashers import make_password

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=["full_name","email","password"]

    def validate(self, attrs):
        attrs["password"]=make_password(attrs["password"])
        return super().validate(attrs)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=["full_name","email","user_type","profile_avatar"]

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=["full_name","profile_avatar"]