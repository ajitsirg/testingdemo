from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Message, GroupChat

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'full_name', 'is_online', 'last_seen')
    list_filter = ('is_online', 'gender', 'city', 'country')
    search_fields = ('username', 'email', 'full_name', 'phone_number')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'email', 'phone_number', 'bio', 'date_of_birth', 'gender', 'city', 'country', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
        ('Status', {'fields': ('is_online', 'last_seen', 'status_message', 'last_login_time')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'full_name', 'phone_number'),
        }),
    )
admin.site.register(CustomUser, CustomUserAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'group', 'content', 'timestamp', 'is_read', 'edited')
    list_filter = ('is_read', 'edited', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'group__name', 'content')
    readonly_fields = ('timestamp',)
admin.site.register(Message, MessageAdmin)



class GroupChatAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'admin__username')
    filter_horizontal = ('members',)  
admin.site.register(GroupChat, GroupChatAdmin)