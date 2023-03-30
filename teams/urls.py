from django.urls import path
from .views import TeamDetailView, TeamView

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<int:team_id>/", TeamDetailView.as_view()),
]