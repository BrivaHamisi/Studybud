from django.contrib import admin
from .models import Room, Topic, Message, User

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'topic', 'updated', 'created')
    list_filter = ('host', 'topic', 'participants', 'created', 'updated')
    search_fields = ('name', 'description', 'host__username', 'topic__name')
    readonly_fields = ('created', 'updated')
    fieldsets = (
        (None, {
            'fields': ('name', 'host', 'topic', 'description', 'participants')
        }),
        ('Timestamps', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )

# admin.site.register(Message)
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'body', 'updated', 'created')
    list_filter = ('room', 'user', 'created', 'updated')
    search_fields = ('body', 'user__username', 'room__name')
    readonly_fields = ('created', 'updated')
    fieldsets = (
        (None, {
            'fields': ('user', 'room', 'body')
        }),
        ('Timestamps', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(User)



