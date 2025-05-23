from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout
import os

@api_view(['GET'])
def api_root(request, format=None):
    # Use the Codespace URL for API root endpoints
    codespace_url = 'https://ubiquitous-pancake-77qqrw5j5v7c7xp-8000.app.github.dev/api/'
    return Response({
        'users': codespace_url + 'users/',
        'teams': codespace_url + 'teams/',
        'activity': codespace_url + 'activity/',
        'leaderboard': codespace_url + 'leaderboard/',
        'workouts': codespace_url + 'workouts/',
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
