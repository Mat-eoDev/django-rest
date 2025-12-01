# API Django REST Framework - Gestion de Concessionnaires et Véhicules

## Description

Bonjour ! Ce projet est une API REST que j'ai développée avec Django REST Framework pour gérer des concessionnaires et leurs véhicules. C'est un devoir que j'ai réalisé pour mon cours.

## Installation

Pour installer et lancer le projet, voici les étapes :

1. D'abord, cloner le dépôt (ou télécharger les fichiers)

2. Créer un environnement virtuel Python :
```bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installer les dépendances nécessaires :
```bash
pip install -r requirements.txt
```

4. Faire les migrations pour créer la base de données :
```bash
python manage.py migrate
```

5. (Optionnel) Créer un superutilisateur pour accéder à l'admin Django :
```bash
python manage.py createsuperuser
```

6. Lancer le serveur de développement :
```bash
python manage.py runserver
```

Une fois lancé, l'API sera accessible sur `http://127.0.0.1:8000/api/`

## Endpoints disponibles

### Endpoints obligatoires

J'ai implémenté les 4 endpoints demandés :

- `GET /api/concessionnaires/` - Récupère la liste de tous les concessionnaires
- `GET /api/concessionnaires/<id>/` - Récupère les détails d'un concessionnaire spécifique
- `GET /api/concessionnaires/<id>/vehicules/` - Liste tous les véhicules d'un concessionnaire
- `GET /api/concessionnaires/<id>/vehicules/<id>/` - Détails d'un véhicule spécifique

### Endpoints bonus (Authentification JWT)

J'ai aussi fait les endpoints bonus pour l'authentification avec JWT :

- `POST /api/users/` - Permet de créer un nouvel utilisateur
  - Body à envoyer : `{"username": "user", "password": "pass", "email": "email@example.com"}`
  
- `POST /api/token/` - Permet d'obtenir un token JWT pour s'authentifier
  - Body à envoyer : `{"username": "user", "password": "pass"}`
  
- `POST /api/refresh_token/` - Permet de rafraîchir un token JWT expiré
  - Body à envoyer : `{"refresh": "refresh_token"}`

## Modèles de données

J'ai créé deux modèles principaux :

### Concessionnaire
- `nom` : Le nom du concessionnaire (max 64 caractères)
- `siret` : Le numéro SIRET (exactement 14 caractères) - **Ce champ n'est pas exposé par l'API** (il est présent en base de données mais pas dans les réponses JSON)

### Véhicule
- `type` : Soit "moto" soit "auto"
- `marque` : La marque du véhicule (max 64 caractères)
- `chevaux` : Le nombre de chevaux (entier)
- `prix_ht` : Le prix hors taxes (nombre décimal)
- `concessionnaire` : Une clé étrangère vers le concessionnaire propriétaire

## Tests

Pour tester l'API, j'ai utilisé Postman mais vous pouvez aussi utiliser Bruno ou n'importe quel autre outil de test d'API REST. Tous les endpoints sont en GET donc c'est assez simple à tester.

## Technologies utilisées

- Django 4.2.7
- Django REST Framework 3.14.0
- djangorestframework-simplejwt 5.3.0 (pour l'authentification JWT)

## Dépôt GitHub

Le projet est disponible sur GitHub. Pour le cloner ou le mettre à jour :

1. Créer un nouveau dépôt sur GitHub (en public)
2. Ajouter le remote :
```bash
git remote add origin https://github.com/VOTRE_USERNAME/VOTRE_REPO.git
```
3. Pousser le code :
```bash
git branch -M main
git push -u origin main
```

Le lien du dépôt GitHub est à fournir dans le rendu du devoir.

