from rest_framework import generics
from django.contrib.auth import get_user_model

from accounts.serializers import UserAppSerializer


UserModel = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserAppSerializer

