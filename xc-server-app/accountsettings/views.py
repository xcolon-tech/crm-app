from rest_framework import generics
from django.contrib.auth.models import User
from .models import Role, Permission, UserRole, RolePermission, AppSettings
from .serializers import (
    UserSerializer, RoleSerializer, PermissionSerializer,
    UserRoleSerializer, RolePermissionSerializer, AppSettingsSerializer
)

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoleListView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class PermissionListView(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class PermissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class UserRoleListView(generics.ListCreateAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

class UserRoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

class AppSettingsView(generics.RetrieveUpdateAPIView):
    queryset = AppSettings.objects.all()
    serializer_class = AppSettingsSerializer

    def get_object(self):
        # Assuming there's only one AppSettings instance.
        return AppSettings.objects.first()