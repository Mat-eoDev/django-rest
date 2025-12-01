from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .views import (
    ConcessionnaireListView,
    ConcessionnaireDetailView,
    ConcessionnaireVehiculesListView,
    ConcessionnaireVehiculeDetailView,
)


@api_view(['POST'])
def create_user(request):
    """
    Endpoint bonus pour créer un utilisateur.
    POST /api/users/
    """
    from django.contrib.auth.models import User
    from django.contrib.auth import authenticate
    
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')
    
    if not username or not password:
        return Response(
            {'error': 'username et password sont requis'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if User.objects.filter(username=username).exists():
        return Response(
            {'error': 'Cet utilisateur existe déjà'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email
    )
    
    return Response(
        {'message': f'Utilisateur {username} créé avec succès', 'user_id': user.id},
        status=status.HTTP_201_CREATED
    )


urlpatterns = [
    # Endpoints obligatoires
    path('concessionnaires/', ConcessionnaireListView.as_view(), name='concessionnaire-list'),
    path('concessionnaires/<int:pk>/', ConcessionnaireDetailView.as_view(), name='concessionnaire-detail'),
    path('concessionnaires/<int:concessionnaire_id>/vehicules/', ConcessionnaireVehiculesListView.as_view(), name='concessionnaire-vehicules'),
    path('concessionnaires/<int:concessionnaire_id>/vehicules/<int:vehicule_id>/', ConcessionnaireVehiculeDetailView.as_view(), name='concessionnaire-vehicule-detail'),
    
    # Endpoints bonus (authentification JWT)
    path('users/', create_user, name='create-user'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token-refresh'),
]

