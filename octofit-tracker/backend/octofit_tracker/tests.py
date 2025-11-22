from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')
        user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes')
        Leaderboard.objects.create(team=marvel, points=1000, rank=1)
        Activity.objects.create(user=user, type='Running', duration=30, calories=300, date='2025-11-22')

    def test_user_team(self):
        user = User.objects.get(email='spiderman@marvel.com')
        self.assertEqual(user.team.name, 'Marvel')

    def test_leaderboard(self):
        marvel = Team.objects.get(name='Marvel')
        leaderboard = Leaderboard.objects.get(team=marvel)
        self.assertEqual(leaderboard.points, 1000)
