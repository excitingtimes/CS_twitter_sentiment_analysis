import numpy as np
import pandas as pd
import multidict as multidict
import matplotlib.pyplot as plt
import dash
import dash_core_components as dcc
import dash_html_components as html
import base64

from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from stop_words import get_stop_words


# liste avg_RTS est une liste contennant les retweets moyen pour chaque candidat
# liste avg_FAVS est une liste contennant les favoris moyen pour chaque candidat
# avg_hashtags est une liste contennat le nombre moyen de hashtags pour chaque candidat
# len_tweet est une liste contennant la longueur moyenne des tweets par candidat
# tweet_sentimental est une liste de liste contennant les sentiments pour chaque candidat ( 0 neg, 1 neutre, 2 positif)

# Adresse du serveur sur lequel les résultats seront affichés : http://127.0.0.1:8050


numberCandidates = 5

def launch_app(analysis): 
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] # Feuille template stylisant l'interface Dash

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets) # Création de l'object application

    app.layout = html.Div(children=[
            html.H1(children='Popularité des candidats'),

            html.Div(children='Graphes de comparaison des popularités de chaque candidat.'),

            dcc.Graph(
                id='graphRts',
                figure={
                'data' : [{'x' : [i], 'y' : [analysis[i - 1]["avg_RT"]], 'type' : 'bar', 'name' : 'Candidat numéro ' + str(i)} for i in range(1, numberCandidates + 1)],
                'layout': {
                'title': 'Nombre moyen de retweets par tweet.'
                }
                }),

            dcc.Graph(
                    id='graphFavs',
                    figure={
                    'data':  [{'x' : [i], 'y' : [analysis[i - 1]["avg_fav"]], 'type' : 'bar', 'name' : 'Candidat numéro ' + str(i)} for i in range(1, numberCandidates + 1)],
                    'layout': {
                    'title': 'Nombre moyen de personnes marquant un tweet conercnant un candidat en tant que favoris.'
                    }
                    }),

            dcc.Graph(
                    id='graphHashtags',
                    figure={
                    'data': [{'x' : [i], 'y' : [analysis[i - 1]["avg_hashtag"]], 'type' : 'bar', 'name' : 'Candidat numéro ' + str(i)} for i in range(1, numberCandidates + 1)],

                    'layout': {
                    'title': 'Nombre moyen de hashtags par candidat.'
                    }
                    }),

            dcc.Graph(
                    id='graphLenTweets',
                    figure={
                    'data': [{'x' : [i], 'y' : [analysis[i - 1]["avg_len_tweets"]], 'type' : 'bar', 'name' : 'Candidat numéro ' + str(i)} for i in range(1, numberCandidates + 1)],
                    'layout': {
                    'title': 'Longueur moyenne des tweets par candidat.'
                    }
                    }),

            dcc.Graph(
                    id='graphSentiments',
                    figure={
                    'data' : [{'x' :  [i], 'y' : [analysis[i - 1]["tweets_neg"], analysis[i - 1]["tweets_neu"], analysis[i - 1]["tweets_pos"]], 'type' : 'bar', 'name' : 'Candidat numéro ' + str(i)} for i in range(1, numberCandidates + 1)],
                    'layout': {
                    'title': 'Graphe de subjectivité des tweets par candidat.'
                    }
                    }),

            html.Div(children='''
                    Tweets négatifs, tweets neutres, tweets positifs.''')
            ])

    app.run_server(debug=True)

"""
def get_frequency(text):
    resultat, tempdict = multidict.MultiDict(), {}

    # On construit le premier dictionnaire temporaire
    for word in text.split(" "):
        val = tempdict.get(word, 0)
        tempdict[word.lower().strip()] = val + 1

    for key in tempdict: # On copie tempdict dans un Multidict
        resultat.add(key, tempdict[key])

    return resultat"""

def nuage(tweets, c = -1): # Fonction affichant le wordcloud associé aux tweets concernant le candidat numéro c
    if c != -1: # Le cas c = -1 correspond à effectuer un wordcloud sur l'ensemble des tweets concernant tous les candidats
        tweets = [t for t in tweets if t["candidat"] == c]

    chaine = ""
    for t in tweets: # Concaténation des tweets pour analyse statistique (wordcloud)
        chaine += t["text"]

    stop_words = get_stop_words('fr')
    
    stopwords = set(stop_words) # Mots à exclure car trop communs
    stopwords.update(["https", "co", "RT"])

    wave_mask = np.array(Image.open("mask.jpg")) # Création du masque

    wordcloud = WordCloud(colormap = "Blues", mask=wave_mask, stopwords = stopwords).generate(chaine) # Création du wordcloud

    #plt.imshow(wordcloud, interpolation='bilinear') # Affichage du wordcloud
    #plt.plot()

    if c == -1: # Sauvegarde du wordcloud
        wordcloud.to_file("candidates.png")
    else:
        wordcloud.to_file("candidate" + str(c) + ".png")

def td_execute(tweets, analysis):
    print("Création du nuage de mots pour l'ensemble des candidats.")
    nuage(tweets)

    for c in range(1, numberCandidates + 1):
        print("Création du nuage de mots pour le candidat " + str(c) + ".")
        nuage(tweets, c)

    launch_app(analysis)
