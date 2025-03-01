from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, EventViewSet, TicketViewSet

router = DefaultRouter()
router.register(r'register', UserViewSet)
router.register(r'events', EventViewSet)
router.register(r'events', TicketViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
