from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    UserListView, UserDetailView,
    MessageCreateView, MessageListView, MessageDetailView,
    GroupChatCreateView, GroupChatListView, GroupChatDetailView
)



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/me/', UserDetailView.as_view(), name='user-detail'),

    path('messages/', MessageCreateView.as_view(), name='message-create'),
    path('messages/list/', MessageListView.as_view(), name='message-list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),

    path('groupchats/', GroupChatCreateView.as_view(), name='groupchat-create'),
    path('groupchats/list/', GroupChatListView.as_view(), name='groupchat-list'),
    path('groupchats/<int:pk>/', GroupChatDetailView.as_view(), name='groupchat-detail'),
]