import json
import pandas as pd


numberCandidates = 5


def store_tweets(tweets,filename): # Fonction enregistrant les tweets dans un fichier json
    with open(filename,"w") as f: #ouverture du fichier
        for t in tweets:
            json.dump(t,f) #ajout de l'élément



def unstore_tweets(filename): # Fonction permettant de récupérer les tweets préalablement stockés dans un ficheir json
	with open(filename,"r") as file : #ouverture du fichier
		tweets=json.load(file) #transformation du fichier json en une liste de listes tweets?
	return tweets



def tableau_donnees(tweet_status): # Fonction auxiliaire
	tweet_json=json.dump(tweet_status[0]) #transformation d'un status en json



def json_to_dataframe(dico_json): # Fonction permettant de transférer des données json en dataframe
	dico_python=json.loads(dico_json) #extraction du dictionnaire de json vers python
	array=pd.DataFrame(dico_python)	#transformation du dico en tableau à l'aide de panda
	return(array) #affichage du tableau



def ts_execute(tweets):
	for c in range(1, numberCandidates + 1):
		store_tweets([t for t in tweets if t["candidat"] == c], "tweets" + str(c) + ".json")
