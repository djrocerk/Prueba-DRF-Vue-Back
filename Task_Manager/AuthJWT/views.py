from django.utils import timezone
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated

# Creacion de la vista para la obtención del JWT y los permisos del usuario
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

# Vista para cerrar sesión y eliminar el token (opcional)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        
        # Eliminacion de la cookie del token
        response = Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        response.delete_cookie('access_token')
        return response