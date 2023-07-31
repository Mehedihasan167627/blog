from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import*
from .models import* 

class HomeAPIView(APIView):
    def get(self,request):
        info_qs=Information.objects.last()
        information_data=InformationSerializer(info_qs,many=False).data

        portfolio=Portfolio.objects.all().order_by("-id")
        portfolio_data=PortfolioSerializer(portfolio,many=True).data

        skill_qs=MySkill.objects.all().order_by("-id")
        skills_data=MySkillSerializer(skill_qs,many=True).data

        data={
            "info":information_data,
            "portfolio":portfolio_data,
            "skills":skills_data
        }
        return Response({"payload":data},status=status.HTTP_200_OK)

