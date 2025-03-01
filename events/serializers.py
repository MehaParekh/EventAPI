from rest_framework import serializers
from .models import User, Event, Ticket
from . import constants

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (constants.ID, constants.USERNAME, constants.PASSWORD, constants.ROLE, constants.IS_STAFF)

    def create(self, validated_data):
        role = validated_data.get(constants.ROLE, constants.USER)
        if role == constants.ADMIN:
            validated_data[constants.IS_STAFF] = True  # Make user an admin (staff)
        user = User.objects.create_user(**validated_data)
        return user

# Event serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (constants.ID, constants.NAME, constants.DATE, constants.TOTAL_TICKET, constants.TICKETS_SOLD)

# Ticket serializer
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (constants.ID, constants.USERS, constants.EVENT, constants.QUANTITY, constants.PURCHASE_DATE)

    def validate_quantity(self, value):
        event = self.initial_data.get(constants.EVENT)
        event = Event.objects.get(id=event)
        if event.tickets_sold + value > event.total_tickets:
            raise serializers.ValidationError(constants.NO_TICKET)
        return value
