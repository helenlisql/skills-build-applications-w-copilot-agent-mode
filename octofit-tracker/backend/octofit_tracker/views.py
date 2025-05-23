from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout
import os

@api_view(['GET', 'POST'])
def api_root(request, format=None):
    # Replace with your actual Codespace name or use an environment variable if set
    codespace_url = os.environ.get('CODESPACE_URL', 'https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev')
    localhost_url = 'http://localhost:8000'
    return Response({
        'users': {
            'codespace': f'{codespace_url}/api/users/?format=api',
            'localhost': f'{localhost_url}/api/users/?format=api',
        },
        'teams': {
            'codespace': f'{codespace_url}/api/teams/?format=api',
            'localhost': f'{localhost_url}/api/teams/?format=api',
        },
        'activities': {
            'codespace': f'{codespace_url}/api/activities/?format=api',
            'localhost': f'{localhost_url}/api/activities/?format=api',
        },
        'leaderboard': {
            'codespace': f'{codespace_url}/api/leaderboard/?format=api',
            'localhost': f'{localhost_url}/api/leaderboard/?format=api',
        },
        'workouts': {
            'codespace': f'{codespace_url}/api/workouts/?format=api',
            'localhost': f'{localhost_url}/api/workouts/?format=api',
        },
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
