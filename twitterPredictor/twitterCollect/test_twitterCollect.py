# Tests unitaires - Module Twitter Collect

import main as tcs

def test1(): # Vérifier si le système crée effectivement une connexion avec l'API
	assert (tcs.twitter_setup() is not None)

def test2(): # Vérifie si le système renvoie effectivement des données sur une requête générale
	assert(tcs.collect("#TPMP", 250) is not None)

def test3(): # Vérifie si le système renvoie effectivement des données sur un utilisateur particulier
	assert(tcs.collect_by_user("EmmanuelMacron", 240) is not None)
