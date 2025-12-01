#!/usr/bin/env python
"""
Script de test pour l'API Django REST Framework
Teste tous les endpoints disponibles
"""
import os
import sys
import django
import requests
import json

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from api.models import Concessionnaire, Vehicule

BASE_URL = "http://127.0.0.1:8000/api"

def print_test(name):
    """Affiche le nom du test"""
    print(f"\n{'='*60}")
    print(f"TEST: {name}")
    print(f"{'='*60}")

def test_endpoint(method, url, data=None, expected_status=200):
    """Teste un endpoint"""
    try:
        if method == "GET":
            response = requests.get(url, timeout=5)
        elif method == "POST":
            response = requests.post(url, json=data, timeout=5)
        else:
            print(f"❌ Méthode {method} non supportée")
            return False
        
        status_ok = response.status_code == expected_status
        status_icon = "✅" if status_ok else "❌"
        
        print(f"{status_icon} {method} {url}")
        print(f"   Status: {response.status_code} (attendu: {expected_status})")
        
        if response.status_code == 200 or response.status_code == 201:
            try:
                data = response.json()
                print(f"   Réponse: {json.dumps(data, indent=2, ensure_ascii=False)}")
            except:
                print(f"   Réponse: {response.text[:200]}")
        else:
            print(f"   Erreur: {response.text[:200]}")
        
        return status_ok
    except requests.exceptions.ConnectionError:
        print(f"❌ {method} {url}")
        print(f"   Erreur: Impossible de se connecter au serveur. Assurez-vous que le serveur Django est lancé.")
        return False
    except Exception as e:
        print(f"❌ {method} {url}")
        print(f"   Erreur: {str(e)}")
        return False

def create_test_data():
    """Crée des données de test"""
    print("\n📝 Création des données de test...")
    
    # Créer des concessionnaires
    conc1, _ = Concessionnaire.objects.get_or_create(
        siret="12345678901234",
        defaults={"nom": "Auto Plus Paris"}
    )
    conc2, _ = Concessionnaire.objects.get_or_create(
        siret="98765432109876",
        defaults={"nom": "Moto Center Lyon"}
    )
    
    # Créer des véhicules
    Vehicule.objects.get_or_create(
        type="auto",
        marque="Peugeot",
        chevaux=120,
        prix_ht=25000.0,
        concessionnaire=conc1
    )
    Vehicule.objects.get_or_create(
        type="moto",
        marque="Yamaha",
        chevaux=80,
        prix_ht=12000.0,
        concessionnaire=conc2
    )
    Vehicule.objects.get_or_create(
        type="auto",
        marque="Renault",
        chevaux=90,
        prix_ht=18000.0,
        concessionnaire=conc1
    )
    
    print("✅ Données de test créées")
    return conc1, conc2

def main():
    """Fonction principale de test"""
    print("\n" + "="*60)
    print("🧪 TESTS DE L'API DJANGO REST FRAMEWORK")
    print("="*60)
    
    # Créer les données de test
    conc1, conc2 = create_test_data()
    
    results = []
    
    # Test 1: Liste des concessionnaires
    print_test("Liste des concessionnaires")
    results.append(("GET /api/concessionnaires/", 
                   test_endpoint("GET", f"{BASE_URL}/concessionnaires/")))
    
    # Test 2: Détails d'un concessionnaire
    print_test("Détails d'un concessionnaire")
    results.append(("GET /api/concessionnaires/<id>/", 
                   test_endpoint("GET", f"{BASE_URL}/concessionnaires/{conc1.id}/")))
    
    # Test 3: Liste des véhicules d'un concessionnaire
    print_test("Liste des véhicules d'un concessionnaire")
    results.append(("GET /api/concessionnaires/<id>/vehicules/", 
                   test_endpoint("GET", f"{BASE_URL}/concessionnaires/{conc1.id}/vehicules/")))
    
    # Test 4: Détails d'un véhicule
    vehicule = Vehicule.objects.first()
    if vehicule:
        print_test("Détails d'un véhicule spécifique")
        results.append(("GET /api/concessionnaires/<id>/vehicules/<id>/", 
                       test_endpoint("GET", f"{BASE_URL}/concessionnaires/{vehicule.concessionnaire.id}/vehicules/{vehicule.id}/")))
    
    # Test 5: Création d'un utilisateur (bonus)
    print_test("Création d'un utilisateur (bonus)")
    # Supprimer l'utilisateur s'il existe déjà
    User.objects.filter(username="testuser").delete()
    test_user_data = {
        "username": "testuser",
        "password": "testpass123",
        "email": "test@example.com"
    }
    results.append(("POST /api/users/", 
                   test_endpoint("POST", f"{BASE_URL}/users/", test_user_data, expected_status=201)))
    
    # Test 6: Obtention d'un token JWT (bonus)
    print_test("Obtention d'un token JWT (bonus)")
    token_data = {
        "username": "testuser",
        "password": "testpass123"
    }
    token_result = test_endpoint("POST", f"{BASE_URL}/token/", token_data, expected_status=200)
    results.append(("POST /api/token/", token_result))
    
    # Récupérer le refresh token pour le test suivant
    refresh_token = None
    if token_result:
        try:
            response = requests.post(f"{BASE_URL}/token/", json=token_data, timeout=5)
            if response.status_code == 200:
                refresh_token = response.json().get("refresh")
        except:
            pass
    
    # Test 7: Rafraîchissement d'un token JWT (bonus)
    if refresh_token:
        print_test("Rafraîchissement d'un token JWT (bonus)")
        refresh_data = {"refresh": refresh_token}
        results.append(("POST /api/refresh_token/", 
                       test_endpoint("POST", f"{BASE_URL}/refresh_token/", refresh_data, expected_status=200)))
    
    # Résumé
    print("\n" + "="*60)
    print("📊 RÉSUMÉ DES TESTS")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for endpoint, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {endpoint}")
    
    print(f"\n✅ Tests réussis: {passed}/{total}")
    if passed == total:
        print("🎉 Tous les tests sont passés avec succès !")
    else:
        print(f"⚠️  {total - passed} test(s) ont échoué")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

