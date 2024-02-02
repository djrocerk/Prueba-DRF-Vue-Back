from django.urls import path
from .views import MyTokenObtainPairView, LogoutView

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),   # endpoint para la obtencion del token
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
