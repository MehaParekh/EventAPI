from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import connection
from . import constants


# User model with role-based access
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = constants.ADMIN
        USER = constants.USER

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER,
    )

    def save(self, *args, **kwargs):
        if self.role == constants.ADMIN:
            self.is_staff = True  # Set is_staff to True for Admins
        super().save(*args, **kwargs)


# Event model
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    total_tickets = models.IntegerField()
    tickets_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Ticket model
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} tickets for {self.event.name}"

#Raw SQL query to fetch the top 3 events by tickets sold
def get_top_events():
    with connection.cursor() as cursor:
        cursor.execute(""" SELECT e.id, e.name, e.total_tickets, e.tickets_sold FROM events_event e ORDER BY 
                        e.tickets_sold DESC LIMIT 3;""")
        return cursor.fetchall()
