from djoser.views import UserViewSet
from rest_framework.pagination import PageNumberPagination

from .serializers import CustomUserSerializer
from .models import User


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    pagination_class = PageNumberPagination
