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



class StartChatSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Chat 
        exclude=("sender","receiver",)

    
    def validate(self, attrs):
        sender=self.context.get("sender")
        attrs["sender"]=sender
        attrs["receiver"]=User.objects.filter(is_superuser=True).last()

        return super().validate(attrs)
    


