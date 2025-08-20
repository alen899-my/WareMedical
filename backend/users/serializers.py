from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','role']

#login Serializer maked
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

    #validating the user
    def validate(self,attrs):
        username=attrs.get('username')
        password=attrs.get('password')
        user=authenticate(username=username,password=password)
        if not user:
            raise serializers.ValidationError("Invalid Credentials")
        refresh=RefreshToken.for_user(user)
        return{
            "refresh":str(refresh),
            "access":str(refresh.access_token),
            "user":UserSerializer(user).data
        }