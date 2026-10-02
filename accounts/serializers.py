from rest_framework import serializers
from django.contrib.auth import get_user_model


UserModel = get_user_model()

class UserAppSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = UserModel
        fields = ['username','password','email']

    def create(self,validated_data):
        return UserModel.objects.create_user(**validated_data)

