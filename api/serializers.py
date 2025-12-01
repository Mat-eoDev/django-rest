from rest_framework import serializers
from .models import Concessionnaire, Vehicule


class ConcessionnaireSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Concessionnaire.
    Le champ siret est exclu (présent en base mais non exposé par l'API).
    """
    class Meta:
        model = Concessionnaire
        fields = ['id', 'nom']
        # Le champ siret est volontairement exclu


class VehiculeSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Véhicule.
    Tous les champs sont inclus.
    """
    class Meta:
        model = Vehicule
        fields = ['id', 'type', 'marque', 'chevaux', 'prix_ht', 'concessionnaire']


class VehiculeDetailSerializer(serializers.ModelSerializer):
    """
    Serializer pour les détails d'un véhicule.
    Inclut les informations du concessionnaire associé.
    """
    concessionnaire = ConcessionnaireSerializer(read_only=True)
    
    class Meta:
        model = Vehicule
        fields = ['id', 'type', 'marque', 'chevaux', 'prix_ht', 'concessionnaire']

