from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with fake data for all endpoints.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        user1 = User.objects.create(name='Alice', email='alice@example.com', team='Team Alpha')
        user2 = User.objects.create(name='Bob', email='bob@example.com', team='Team Beta')

        # Teams
        team1 = Team.objects.create(name='Team Alpha', members=['Alice'])
        team2 = Team.objects.create(name='Team Beta', members=['Bob'])

        # Activities
        Activity.objects.create(user='Alice', activity='Running', duration=30)
        Activity.objects.create(user='Bob', activity='Cycling', duration=45)

        # Leaderboard
        Leaderboard.objects.create(team='Team Alpha', points=100)
        Leaderboard.objects.create(team='Team Beta', points=80)

        # Workouts

        self.stdout.write(self.style.SUCCESS('Database populated with fake data.'))
