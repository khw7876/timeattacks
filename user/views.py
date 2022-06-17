from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from django.contrib.auth import authenticate, login, logout

# Create your views here.
class UserAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def sign_up(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password = password)
        if user:
            return Response({"message" : "이미 존재하는 계정입니다!!"})
        user.save()
        return Response({"message" : "회원가입 되었습니다!!"})

    def delete(self, request):
        logout(request)
        return Response({"message" : "logout success!!"})