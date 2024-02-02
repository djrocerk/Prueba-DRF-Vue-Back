from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Users
from .serializers import UserRegistrationSerializer, UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user