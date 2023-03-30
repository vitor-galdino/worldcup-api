from django.forms.models import model_to_dict
from rest_framework.views import APIView, Response, status

from teams.exceptions import (ImpossibleTitlesError, InvalidYearCupError,
                              NegativeTitlesError)

from .models import Team
from .utils import data_processing


class TeamView(APIView):
    def post(self, request):
        try:
            data_processing(request.data)
            team = Team.objects.create(**request.data)

        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as err:
            return Response({"error": str(err)}, status.HTTP_400_BAD_REQUEST)
        
        return Response(model_to_dict(team), status.HTTP_201_CREATED)
    
    def get(self, request):
        teams = Team.objects.all()
        teams_list = [model_to_dict(team) for team in teams]

        return Response(teams_list, status.HTTP_200_OK)
    
class TeamDetailView(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)

        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        
        return Response(model_to_dict(team))
    
    def delete(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        
        for key, value in request.data.items():
            setattr(team, key, value)
        
        team.save()
        return Response(model_to_dict(team))