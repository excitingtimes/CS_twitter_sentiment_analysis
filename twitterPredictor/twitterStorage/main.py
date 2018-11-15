<<<<<<< HEAD
#étape 1

import json
import pandas as pd


def store_tweets(tweets,filename):
	with open(filename,"w") as file:		#ouverture du fichier
		for a in tweets:			#a est une liste de chaîne de caractères
			json.dump(a,file)		#ajout de l'élément



def unstore_tweets(filename):
	with open(filename,"r") as file:		#ouverture du fichier
		tweets=json.load(file)			#transformation du fichier json en une liste de listes tweets?
	return tweets


#étape2


def tableau_donnees(tweet_status):
	tweet_json=json.dump(tweet_status[0])		#transformation d'un status en json


def json_to_dataframe(dico_json):
	dico_python=json.loads(dico_json)		#extraction du dictionnaore de json vers python
	array=pd.DataFrame(dico_python)			#transformation du dico en tableau à l'aide de panda
	return(array)					#affichage du tableau


=======
def execute():
>>>>>>> 16ff165d25629c76cf78e19ca385bdeca8dce6ce
