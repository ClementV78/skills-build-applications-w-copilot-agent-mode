from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for development'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = []
        user_data = [
            {'email': 'thundergod@mhigh.edu', 'name': 'Thor', 'age': 30},
            {'email': 'metalgeek@mhigh.edu', 'name': 'Tony Stark', 'age': 35},
            {'email': 'zerocool@mhigh.edu', 'name': 'Steve Rogers', 'age': 32},
            {'email': 'crashoverride@mhigh.edu', 'name': 'Natasha Romanoff', 'age': 28},
            {'email': 'sleeptoken@mhigh.edu', 'name': 'Bruce Banner', 'age': 40},
        ]
        for data in user_data:
            user = User.objects.create(**data)
            users.append(user)
            self.stdout.write(f'Created user: {user.name}')

        # Create teams
        blue_team = Team.objects.create(name='Blue Team')
        gold_team = Team.objects.create(name='Gold Team')
        
        # Add members to teams
        blue_team.members.add(users[0], users[1], users[2])
        gold_team.members.add(users[3], users[4])
        self.stdout.write(f'Created teams: Blue Team, Gold Team')

        # Create activities
        for user in users:
            Activity.objects.create(
                user=user,
                activity_type='Running',
                duration=60,
                date=datetime.now().date()
            )
        self.stdout.write('Created activities for users')

        # Create leaderboard entries
        for team in [blue_team, gold_team]:
            Leaderboard.objects.create(
                team=team,
                points=100 if team.name == 'Blue Team' else 90
            )
        self.stdout.write('Created leaderboard entries')

        # Create workouts
        workout_data = [
            {'name': 'Morning Run', 'description': 'Early morning cardio session', 'duration': 30},
            {'name': 'Strength Training', 'description': 'Full body workout', 'duration': 45},
            {'name': 'HIIT', 'description': 'High-intensity interval training', 'duration': 20},
            {'name': 'Yoga Flow', 'description': 'Flexibility and balance', 'duration': 60},
            {'name': 'Core Workout', 'description': 'Ab and core strengthening', 'duration': 15},
        ]
        for data in workout_data:
            Workout.objects.create(**data)
        self.stdout.write('Created workouts')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
