from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.timezone import now


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(null=True, blank=True)
    status_message = models.CharField(max_length=255, blank=True, null=True)
    last_login_time = models.DateTimeField(null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups", 
        blank=True,
        verbose_name="groups",
        help_text="The groups this user belongs to.",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_user_permissions", 
        blank=True,
        verbose_name="user permissions",
        help_text="Specific permissions for this user.",
    )

    def __str__(self):
        return f"{self.full_name or self.username} - {'Online' if self.is_online else 'Offline'}"


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages', null=True, blank=True)
    group = models.ForeignKey('GroupChat', on_delete=models.CASCADE, related_name='group_messages', null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    deleted_for = models.ManyToManyField(CustomUser, related_name='deleted_messages', blank=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver or self.group}: {self.content[:20]}"

    class Meta:
        ordering = ['-timestamp']


class GroupChat(models.Model):
    name = models.CharField(max_length=255)
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='admin_groups')
    members = models.ManyToManyField(CustomUser, related_name='group_chats')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']