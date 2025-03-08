from django.urls import path
from .views import MessageListCreateView, GroupChatListCreateView

urlpatterns = [
    path('messages/', MessageListCreateView.as_view(), name='messages'),
    path('groups/', GroupChatListCreateView.as_view(), name='group_chats'),
]
