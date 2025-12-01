from django.contrib import admin
from .models import Concessionnaire, Vehicule


@admin.register(Concessionnaire)
class ConcessionnaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'siret')
    search_fields = ('nom', 'siret')


@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('marque', 'type', 'chevaux', 'prix_ht', 'concessionnaire')
    list_filter = ('type', 'concessionnaire')
    search_fields = ('marque',)

