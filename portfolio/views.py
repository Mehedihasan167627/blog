from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions

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



class StartChatAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        receiver=User.objects.filter(is_superuser=True).last()
        chats=Chat.get_messages(sender=request.user,receiver=receiver)
        chat_list=[]
        for chat in chats:
            chat_list.append({
                  "id":chat.id,
                "sender":chat.sender.full_name,
                "message":chat.message,
                "receiver":chat.receiver.full_name,
                "created_at":chat.created_at
            })
        
        return Response({"chat":chat_list})


    
    def post(self,request):
        serializer=StartChatSerailizer(data=request.data,context={"sender":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"msg send sucessfully"})
        return Response({"errors":serializer.errors})