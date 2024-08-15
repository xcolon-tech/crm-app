from django.urls import path
from .views import (
    UserListView, UserDetailView,
    RoleListView, RoleDetailView,
    PermissionListView, PermissionDetailView,
    UserRoleListView, UserRoleDetailView,
    AppSettingsView
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('roles/', RoleListView.as_view(), name='role-list'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='role-detail'),

    path('permissions/', PermissionListView.as_view(), name='permission-list'),
    path('permissions/<int:pk>/', PermissionDetailView.as_view(), name='permission-detail'),

    path('user-roles/', UserRoleListView.as_view(), name='user-role-list'),
    path('user-roles/<int:pk>/', UserRoleDetailView.as_view(), name='user-role-detail'),

    path('app-settings/', AppSettingsView.as_view(), name='app-settings'),
]