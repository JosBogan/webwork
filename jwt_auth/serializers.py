from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password

from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'Does Not Match'})
        
        data['password'] = make_password(password)

        return data


    class Meta:
        model = User
        fields = '__all__'