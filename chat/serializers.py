from .models import Message, GroupChat, CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'full_name', 'phone_number', 'bio', 'date_of_birth', 'gender', 
            'city', 'country', 'created_at', 'updated_at', 'avatar', 'is_online', 'last_seen',
            'status_message', 'last_login_time'
        ]
        read_only_fields = ['created_at', 'updated_at', 'last_seen', 'last_login_time']

    def update(self, instance, validated_data):
        instance.status_message = validated_data.get('status_message', instance.status_message)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class GroupChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChat
        fields = '__all__'