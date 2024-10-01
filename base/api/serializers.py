from rest_framework.serializers import ModelSerializer
from base.models import *


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ('id',)
