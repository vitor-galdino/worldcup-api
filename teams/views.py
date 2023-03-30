from django.forms.models import model_to_dict
from rest_framework.views import APIView, Response, status

from .models import Team


class TeamView(APIView):
    def post(self, request):
        team = Team.objects.create(**request.data)
        return Response(model_to_dict(team), status.HTTP_201_CREATED)