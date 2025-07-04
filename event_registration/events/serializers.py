from rest_framework import serializers
from .models import Event,Registration


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__' # this will include each fields



class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
        read_only_fields = ['user', 'timestamp']
        