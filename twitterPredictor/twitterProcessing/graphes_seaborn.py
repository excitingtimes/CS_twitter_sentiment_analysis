#fonctions seaborn pour présenter les données
# pour transformer un dico python en dataframe panda: pd.DataFrame()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors
sns.set(style="darkgrid")


#fonction 1: représentation du nombre de tweets concernant un candidat donné en fonction du temps.

def tweets_candidate_survey(tweets_candidate):


def likes_and_retweets(tweets):

#la fonction prend en argument la liste de tous les tweets et renvoie la proportion de like/retweets pour les tweets, en associant une couleur à un candidat donné.

    tweets_dataframe=pd.DataFrame(tweets)
    sns.swarmplot(x="RTS",y="favs", hue="candidat", data=tweets_dataframe)

#graphe renvoyé

def status_to_dataframe(tweets_status):
     tweet_json=json.dump(tweet_status[0])
     tweet_python=json.loads(tweet_json)
     tweet_dataframe=pd.DataFrame(tweet_python)
     return(tweet_dataframe)
 
