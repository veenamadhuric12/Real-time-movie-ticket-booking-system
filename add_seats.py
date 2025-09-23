# app/management/commands/add_seats.py

from django.core.management.base import BaseCommand
from app.models import ShowTime, Seat

class Command(BaseCommand):
    help = 'Add seats for showtimes where seats do not yet exist'

    def handle(self, *args, **options):
        showtimes = ShowTime.objects.all()
        total_created = 0
        for showtime in showtimes:
            if not Seat.objects.filter(show_time=showtime).exists():
                for row in range(1, 6):  # Rows A-E
                    for num in range(1, 11):  # 10 seats per row
                        Seat.objects.create(
                            show_time=showtime,
                            row=chr(64 + row),  # Converts 1 to 'A', 2 to 'B', etc.
                            number=num,
                            is_booked=False
                        )
                        total_created += 1
                self.stdout.write(self.style.SUCCESS(f"Added seats for showtime id {showtime.id}"))
        if total_created == 0:
            self.stdout.write("No new seats were added. All showtimes already have seats.")
        else:
            self.stdout.write(self.style.SUCCESS(f"Total seats created: {total_created}"))
