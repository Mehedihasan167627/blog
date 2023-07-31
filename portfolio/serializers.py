from rest_framework import serializers
from .models import*


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Portfolio
        fields="__all__"


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Information
        fields="__all__"

class MySkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=MySkill
        fields="__all__"