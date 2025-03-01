from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Event, Ticket
from .serializers import UserSerializer, EventSerializer, TicketSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from . import constants

# User Registration View
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=[constants.METHOD_POST])
    def register(self, request):
        return self.create(request)

# Event Management (Admin only)
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminUser]  # Only Admin can manage events

# Ticket Purchase (User only)
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=[constants.METHOD_POST])
    def purchase(self, request, pk=None):
        event = Event.objects.get(id=pk)
        quantity = request.data.get(constants.QUANTITY)

        # Validate ticket quantity
        if event.tickets_sold + int(quantity) > event.total_tickets:
            return Response({constants.DETAIL: constants.NO_TICKET}, status=constants.BAD_REQUEST)

        # Create the ticket
        ticket = Ticket.objects.create(user=request.user, event=event, quantity=quantity)
        event.tickets_sold += int(quantity)
        event.save()

        return Response(TicketSerializer(ticket).data, status=constants.CREATED)

