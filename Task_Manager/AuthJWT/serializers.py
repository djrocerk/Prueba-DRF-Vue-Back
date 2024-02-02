from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Serializador para el formateo de los datos, de la obtencion del token y los permisos
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['permissions'] = self.user.get_all_permissions()
        return data
