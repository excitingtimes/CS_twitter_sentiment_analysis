# Twitter Predictor
# coding: utf-8

# Code principal

from twitterCollect.main import *
from twitterStorage.main import *
from twitterDisplay.main import *
from twitterProcessing.main import *

# Put your credentials file here -----

tweets = tc_execute() # Récupération d'une liste de tweets représentés chacun par un dictionnaire
ts_execute(tweets) # stockage des tweets pour une utilisation ultérieure
analysis = tp_execute(tweets) # renvoie un dictionnaire composé des analyses effectuées sur l'ensemble des tweets

td_execute(tweets, analysis) # affiche l'ensemble des résultats
