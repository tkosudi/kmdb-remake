from django.contrib.auth.models import User
from rest_framework import generics

from accounts.serializers import 

class AccountView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer