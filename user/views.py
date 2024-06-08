from django.shortcuts import render
from rest_framework.views import APIView
import re
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from django.contrib.auth import authenticate,login
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from django.contrib.auth.hashers import make_password
from math import ceil

# Create your views here.
class UserCreateAPI(APIView):
    def get(self,request,format =None):
        user = User.objects.filter(is_active =True)
        return Response({"data":UserSerializer(user,many=True).data}, status=status.HTTP_201_CREATED)

    def post(self,request,format=None):
        data =request.data
        if 'first_name' in data:
            first_name =data['first_name']
        if 'last_name' in data:
            last_name =data['last_name']
        if 'username' in data:
            username =data['username']
        mobile =data['mobile']
        if 'email' in data:
            email = data['email']
        password = data['password']
        existing_user = User.objects.filter(mobile=mobile).first()
        if existing_user:
            return Response({"message": "User with this mobile number already exists."}, status=status.HTTP_400_BAD_REQUEST)

        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            return Response({"message": "Password must contain at least one character, one numeric digit,one special character,and be at least 8 characters long."}, status=400)
        user_= User.objects.get_or_create(mobile=mobile)[0]
        user_.set_password(password)
        user_.save()
        token=Token.objects.create(user = user_).key
        return Response({"data":UserSerializer(user_).data,"message": "User created successfully","token":token}, status=status.HTTP_201_CREATED)


class LoginUserAPI(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        login(request,request.user)
        context = {
            'user_id': request.user.id,
            'username': UserSerializer(request.user).data
        }
        if request.user.is_staff or request.user.is_superuser:
            context['token'] = request.user.get_user_token()
        return Response(context, status = status.HTTP_200_OK)