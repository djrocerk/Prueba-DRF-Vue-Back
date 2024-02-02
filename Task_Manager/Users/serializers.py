from rest_framework import serializers
from .models import Users

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        user = Users.objects.create_user(**validated_data)
        return user
    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
        }

    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'first_name', 'last_name')