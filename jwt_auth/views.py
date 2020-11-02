from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.status import HTTP_422_UNPROCESSABLE_ENTITY
from .serializers import UserSerializer

import jwt

from datetime import datetime, timedelta

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.


class RegisterView(APIView):

    def post(self, request):
        serialized_user = UserSerializer(data=request.data)
        # print(serialized_user)
        if serialized_user.is_valid():
            # print(serialized_user.data)
            serialized_user.save()
            return Response({'message': 'registration sucessful'})

        return Response(serialized_user.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)


class LoginView(APIView):

    def post(self, request):
        print(request.data)

        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)

            if not user.check_passowrd(password):
                raise PermissionDenied({{'message': 'invalid credentials'}})

            dt = datetime.now() + timedelta(days=7)

            token = jwt.encode({'sub': user.id, 'exp': int(dt.strftime('%s'))}, settings.SECRET_KEY, algorithm='HS256')
            return Response({'token': token, 'message': f'Welcome back {user.username}'})

        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid Credentials'})


class ListView(APIView):

    def get(self, _request):
        users = User.objects.all()
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data)