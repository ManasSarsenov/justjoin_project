from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


@extend_schema(tags=['auth'])
class CustomTokenObtainPairView(TokenObtainPairView):
    pass
    # serializer_class = CustomTokenObtainPairSerializer


@extend_schema(tags=['auth'])
class CustomTokenRefreshView(TokenRefreshView):
    pass
