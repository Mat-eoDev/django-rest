from django.db import models
from django.core.exceptions import ValidationError


class Concessionnaire(models.Model):
    """
    Modèle représentant un concessionnaire.
    Le champ siret est stocké en base mais ne sera pas exposé par l'API.
    """
    nom = models.CharField(max_length=64)
    siret = models.CharField(max_length=14, unique=True)
    
    class Meta:
        verbose_name = "Concessionnaire"
        verbose_name_plural = "Concessionnaires"
    
    def clean(self):
        """Validation : le SIRET doit faire exactement 14 caractères."""
        if len(self.siret) != 14:
            raise ValidationError({'siret': 'Le SIRET doit contenir exactement 14 caractères.'})
    
    def save(self, *args, **kwargs):
        """Surcharge de save pour appeler clean() avant la sauvegarde."""
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nom


class Vehicule(models.Model):
    """
    Modèle représentant un véhicule.
    Un véhicule est lié à un concessionnaire.
    """
    TYPE_CHOICES = [
        ('moto', 'Moto'),
        ('auto', 'Auto'),
    ]
    
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    marque = models.CharField(max_length=64)
    chevaux = models.IntegerField()
    prix_ht = models.FloatField()
    concessionnaire = models.ForeignKey(
        Concessionnaire,
        on_delete=models.CASCADE,
        related_name='vehicules'
    )
    
    class Meta:
        verbose_name = "Véhicule"
        verbose_name_plural = "Véhicules"
    
    def __str__(self):
        return f"{self.marque} ({self.type})"

