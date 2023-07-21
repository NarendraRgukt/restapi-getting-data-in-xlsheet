from rest_framework.generics import RetrieveUpdateAPIView,CreateAPIView
from rest_framework import authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from account import serializers

class UserCreate(CreateAPIView):
    serializer_class=serializers.UserSerializer

class UserManage(RetrieveUpdateAPIView):
    serializer_class=serializers.UserSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user

class UserToken(ObtainAuthToken):
    serializer_class=serializers.UserTokenSerializer
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES
    



    