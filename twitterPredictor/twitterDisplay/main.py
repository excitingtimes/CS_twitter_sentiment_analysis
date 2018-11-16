import numpy as np
import pandas as pd
import multidict as multidict
import matplotlib.pyplot as plt

from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

from stop_words import get_stop_words

stop_words = get_stop_words('fr')

numberCandidates = 3

def get_frequency(text):
    resultat, tempdict = multidict.MultiDict(), {}

    # On construit le premier dictionnaire temporaire
    for word in text.split(" "):
        val = tempdict.get(word, 0)
        tempdict[word.lower().strip()] = val + 1

    for key in tempdict: # On copie tempdict dans un Multidict
        resultat.add(key, tempdict[key])

    return resultat

def nuage(tweets, c = -1): # Fonction affichant le wordcloud associé aux tweets concernant le candidat numéro c
    if c != -1: # Le cas c = -1 correspond à effectuer un wordcloud sur l'ensemble des tweets concernant tous les candidats
        tweets = [t for t in tweets if t["candidat"] == c]

    chaine = ""
    for t in tweets: # Concaténation des tweets pour analyse statistique (wordcloud)
        chaine += t["text"]
    
    stopwords = set(stop_words) # Mots à exclure car trop communs
    stopwords.update(["https", "co", "RT"])

    wave_mask = np.array(Image.open("mask.jpg")) # Création du masque

    wordcloud = WordCloud(colormap = "Blues", mask=wave_mask, stopwords = stopwords).generate_from_frequencies(get_frequency(chaine)) # Création du wordcloud

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
