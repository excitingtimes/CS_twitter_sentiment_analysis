# Twitter Predictor

# Code principal

import twitterCollect as tc
import twitterStorage as ts
import twitterDisplay as td
import twitterProcessing as tp

tweets = tc.execute() # Récupération d'une liste de tweets représentés chacun par un dictionnaire
ts.execute(tweets) # stockage des tweets pour une utilisation ultérieure
analysis = tp.execute(tweets) # renvoie un dictionnaire composé des analyses effectuées sur l'ensemble des tweets
td.execute(analysis, tweets) # affiche l'ensemble des résultats
