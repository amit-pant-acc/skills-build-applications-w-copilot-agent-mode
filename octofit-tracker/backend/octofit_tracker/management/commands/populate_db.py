from django.core.management.base import BaseCommand
from django.utils import timezone
from octofit_tracker.models import Team, User, Activity, Workout, LeaderboardEntry


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        LeaderboardEntry.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Sample superhero users
        heroes = [
            {'first_name': 'Peter', 'last_name': 'Parker', 'email': 'peter@marvel.com', 'team': marvel},
            {'first_name': 'Tony', 'last_name': 'Stark', 'email': 'tony@marvel.com', 'team': marvel},
            {'first_name': 'Bruce', 'last_name': 'Wayne', 'email': 'bruce@dc.com', 'team': dc},
            {'first_name': 'Clark', 'last_name': 'Kent', 'email': 'clark@dc.com', 'team': dc},
        ]

        users = []
        for h in heroes:
            u = User.objects.create(**h)
            users.append(u)

        # Create activities and workouts
        today = timezone.now().date()
        for i, u in enumerate(users):
            Activity.objects.create(user=u, name='Run', duration_minutes=30 + i * 10, calories=200 + i * 50, date=today)
            Workout.objects.create(user=u, title='Full Body', exercises=['push', 'pull', 'legs'], date=today)
            LeaderboardEntry.objects.create(user=u, score=100 - i * 10)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with sample data'))
