# API Django REST Framework - Gestion de Concessionnaires et Véhicules

## Description

Ce projet est une API REST développée avec Django REST Framework pour gérer des concessionnaires et leurs véhicules.

## Installation

1. Cloner le dépôt
2. Créer un environnement virtuel :
```bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

4. Effectuer les migrations :
```bash
python manage.py migrate
```

5. Créer un superutilisateur (optionnel) :
```bash
python manage.py createsuperuser
```

6. Lancer le serveur de développement :
```bash
python manage.py runserver
```

L'API sera accessible sur `http://127.0.0.1:8000/api/`

## Endpoints disponibles

### Endpoints obligatoires

- `GET /api/concessionnaires/` - Liste tous les concessionnaires
- `GET /api/concessionnaires/<id>/` - Détails d'un concessionnaire
- `GET /api/concessionnaires/<id>/vehicules/` - Liste des véhicules d'un concessionnaire
- `GET /api/concessionnaires/<id>/vehicules/<id>/` - Détails d'un véhicule spécifique

### Endpoints bonus (Authentification JWT)

- `POST /api/users/` - Créer un utilisateur
  - Body: `{"username": "user", "password": "pass", "email": "email@example.com"}`
  
- `POST /api/token/` - Obtenir un token JWT
  - Body: `{"username": "user", "password": "pass"}`
  
- `POST /api/refresh_token/` - Rafraîchir un token JWT
  - Body: `{"refresh": "refresh_token"}`

## Modèles de données

### Concessionnaire
- `nom` (CharField, max 64 caractères)
- `siret` (CharField, 14 caractères exactement) - **Non exposé par l'API**

### Véhicule
- `type` (Choix: "moto" ou "auto")
- `marque` (CharField, max 64 caractères)
- `chevaux` (IntegerField)
- `prix_ht` (FloatField)
- `concessionnaire` (ForeignKey vers Concessionnaire)

## Tests

Vous pouvez tester les endpoints avec des outils comme Postman ou Bruno.

## Technologies utilisées

- Django 4.2.7
- Django REST Framework 3.14.0
- djangorestframework-simplejwt 5.3.0

## Dépôt GitHub

Pour créer le dépôt GitHub :

1. Créer un nouveau dépôt sur GitHub (public)
2. Ajouter le remote :
```bash
git remote add origin https://github.com/VOTRE_USERNAME/VOTRE_REPO.git
```
3. Pousser le code :
```bash
git branch -M main
git push -u origin main
```

Le lien du dépôt doit être fourni dans le rendu du devoir.

