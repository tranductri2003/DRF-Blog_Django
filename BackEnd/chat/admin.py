from django.contrib import admin
from .models import Room, Message

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description','private', 'get_participants') 
    def get_participants(self, obj):
        return [participant.user_name for participant in obj.participants.all()]
        # data=[]
        # for participant in obj.participants.all():
        #     data.append(participant.user_name)
        # return data
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room','get_slug', 'content', 'created_on')
    def get_slug(self,obj):
        return obj.room.slug