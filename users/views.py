from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *

class RegisterAPIView(APIView):
    def post(self,request,format=None):
        serializer=UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"User register successfully!!"})

        return Response({"errors":serializer.errors})
    

class ProfileAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format=None):
        user=User.objects.get(id=request.user.id)
        serializer=ProfileSerializer(user,many=False) 
        return Response(serializer.data)
    
    def put(self,request,format=None):
        serializer=ProfileUpdateSerializer(data=request.data,instance=request.user) 
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Profile updated successfully","data":serializer.data})
        return Response({"errors":serializer.errors})

