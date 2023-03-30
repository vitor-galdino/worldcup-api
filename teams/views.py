from django.forms.models import model_to_dict
from rest_framework.views import APIView, Response, status

from teams.exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError

from .utils import data_processing
from .models import Team


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