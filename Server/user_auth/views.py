from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from user_auth.models import *
from rest_framework.views import APIView
from django.db import transaction

class SignUpView(APIView):

     def post(self , request , format=None):
        username =  request.data['username']
        password = request.data['password']
        contact_num = request.data['contact']
        email_id = request.data['email_id']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        with transaction.atomic():
            user = User.objects.create_user(username=username , password=password , email=email_id , first_name = first_name , last_name=last_name)
            Person.objects.create(user = user , contact=contact_num)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
 
