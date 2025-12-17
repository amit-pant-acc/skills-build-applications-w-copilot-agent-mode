from django.test import TestCase
from .models import Team, User, Activity, Workout, LeaderboardEntry
from django.utils import timezone

class ModelSmokeTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='testers')
        self.user = User.objects.create(first_name='Test', last_name='User', email='test@example.com', team=self.team)

    def test_create_activity(self):
        a = Activity.objects.create(user=self.user, name='Test Activity', duration_minutes=10, calories=50, date=timezone.now().date())
        self.assertEqual(a.user, self.user)

    def test_create_workout(self):
        w = Workout.objects.create(user=self.user, title='Test Workout', exercises=['squat'], date=timezone.now().date())
        self.assertEqual(w.user, self.user)

    def test_leaderboard_entry(self):
        l = LeaderboardEntry.objects.create(user=self.user, score=42)
        self.assertEqual(l.user, self.user)
