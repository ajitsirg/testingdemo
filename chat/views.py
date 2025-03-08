from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .models import CustomUser, Message, GroupChat
from .serializers import CustomUserSerializer, MessageSerializer, GroupChatSerializer



class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(sender=user) | Message.objects.filter(receiver=user)


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        message = self.get_object()
        if message.sender != self.request.user:
            return Response({"detail": "You do not have permission to edit this message."}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.sender != user and instance.receiver != user:
            return Response({"detail": "You do not have permission to delete this message."}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()


# GroupChat Views
class GroupChatCreateView(generics.CreateAPIView):
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        group = serializer.save(admin=self.request.user)
        group.members.add(self.request.user)


class GroupChatListView(generics.ListAPIView):
    serializer_class = GroupChatSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GroupChat.objects.filter(members=self.request.user)


class GroupChatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        group = self.get_object()
        if group.admin != self.request.user:
            return Response({"detail": "You do not have permission to update this group."}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()

    def perform_destroy(self, instance):
        if instance.admin != self.request.user:
            return Response({"detail": "You do not have permission to delete this group."}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()