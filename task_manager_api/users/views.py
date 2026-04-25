from rest_framework import generics, permissions

from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    """Представление для регистрации нового пользователя."""

    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
