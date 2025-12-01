from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Concessionnaire, Vehicule
from .serializers import (
    ConcessionnaireSerializer,
    VehiculeSerializer,
    VehiculeDetailSerializer
)


class ConcessionnaireListView(APIView):
    """
    Vue pour lister tous les concessionnaires.
    GET /api/concessionnaires/
    """
    def get(self, request):
        concessionnaires = Concessionnaire.objects.all()
        serializer = ConcessionnaireSerializer(concessionnaires, many=True)
        return Response(serializer.data)


class ConcessionnaireDetailView(APIView):
    """
    Vue pour obtenir les détails d'un concessionnaire.
    GET /api/concessionnaires/<id>/
    """
    def get(self, request, pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=pk)
        serializer = ConcessionnaireSerializer(concessionnaire)
        return Response(serializer.data)


class ConcessionnaireVehiculesListView(APIView):
    """
    Vue pour lister tous les véhicules d'un concessionnaire.
    GET /api/concessionnaires/<id>/vehicules/
    """
    def get(self, request, concessionnaire_id):
        concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_id)
        vehicules = Vehicule.objects.filter(concessionnaire=concessionnaire)
        serializer = VehiculeSerializer(vehicules, many=True)
        return Response(serializer.data)


class ConcessionnaireVehiculeDetailView(APIView):
    """
    Vue pour obtenir les détails d'un véhicule spécifique d'un concessionnaire.
    GET /api/concessionnaires/<id>/vehicules/<id>/
    """
    def get(self, request, concessionnaire_id, vehicule_id):
        concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_id)
        vehicule = get_object_or_404(
            Vehicule,
            pk=vehicule_id,
            concessionnaire=concessionnaire
        )
        serializer = VehiculeDetailSerializer(vehicule)
        return Response(serializer.data)

