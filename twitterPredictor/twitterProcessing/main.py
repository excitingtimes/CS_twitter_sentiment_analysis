numberCandidates = 3

def avg_RT(tweets_candidat):
    """compte le nombre moyen de reweets par candidat"""
    nombre_tweets=len(tweets_candidat)
    RTStotal=0
    for a in tweets_candidat: #parcourt la liste de tweet pour compter le nombre total de retweets (RTS)
        RTStotal+=a["RTS"]
    return(RTStotal/nombre_tweets)
    
def max_RT(tweets_candidat):
    """compte le nombre maximal de reweets par candidat"""
    maxRTS=tweets_candidat[0]["RTS"]
    for a in tweets_candidat:  #cherche le nombre maximal de Retweets (RTS) pour un candidat donné
        if a["RTS"]>=maxRTS:
            maxRTS=a["RTS"]
    return(maxRTS)
    
def min_RT(tweets_candidat):
    """compte le nombre minimal de reweets par candidat"""
    minRTS=tweets_candidat[0]["RTS"]
    for a in tweets_candidat:  #cherche le nombre minimal de Retweets (RTS) pour un candidat donné
        if a["RTS"]<=minRTS:
            minRTS=a["RTS"]
    return(minRTS)
    
def avg_fav(tweets_candidat):
    """compte le nombre moyen de favoris par candidat"""
    nombre_tweets=len(tweets_candidat)
    favstotal=0
    for a in tweets_candidat: #parcourt la liste de tweet pour compter le nombre total de favoris (favs)
        favstotal+=a["favs"]
    return(favstotal/nombre_tweets)
    
def max_fav(tweets_candidat):
    """compte le nombre maximal de favoris par candidat"""
    maxfavs=tweets_candidat[0]["favs"]
    for a in tweets_candidat:  #cherche le nombre maximal de favoris (favs) pour un candidat donné
        if a["favs"]>=maxfavs:
            maxfavs=a["favs"]
    return(maxfavs)
    
def min_fav(tweets_candidat):
    """compte le nombre minimal de favoris par candidat"""
    minfavs=tweets_candidat[0]["favs"]
    for a in tweets_candidat:  #cherche le nombre minimal de favoris (favs) pour un candidat donné
        if a["favs"]<=minfavs:
            minRTS=a["favs"]
    return(minfavs)
    
def len_tweet(tweet):
    """calcule la longueur d'un tweet"""
    return(len(tweet["text"]))
    
def avg_len_tweets(tweets_candidat):
    """calcule la longueur moyenne des tweets pour un candidat"""
    nombre_tweets=len(tweets_candidat)
    nombre_carac_total=0
    for a in tweets_candidat: #parcourt la liste de tweet pour compter le nombre total de caractères
        len_a=len_tweet(a)
        nombre_carac_total+=len_a
    return(nombre_carac_total/nombre_tweets)
    
def max_len_tweets(tweets_candidat):
    """calcule la longueur maximale des tweets pour un candidat"""
    max_len_tweet=len_tweet(tweets_candidat[0])
    for a in tweets_candidat:   #cherche la longueur maximale d'un tweet pour un candidat donné
        len_a=len_tweet(a)
        if len_a>=max_len_tweet:
            max_len_tweet=len_a
    return(max_len_tweet)
    
def min_len_tweets(tweets_candidat):
    """calcule la longueur minimale des tweets pour un candidat"""
    min_len_tweet=len_tweet(tweets_candidat[0])
    for a in tweets_candidat:  #cherche la longueur minimale d'un tweet pour un candidat donné
        len_a=len_tweet(a)
        if len_a<=min_len_tweet:
            min_len_tweet=len_a
    return(min_len_tweet)
    
def len_hashtag(tweet):
    """calcule le nombre de hashtags dans un tweet"""
    liste_des_hashtags=tweet["hashtags"]
    return(len(liste_des_hashtags))
    
def min_hashtag(tweets_candidat):
    """compte le nombre minimal de hashtags par candidat dans un tweet"""
    min_hashtags=len_hashtag(tweets_candidat[0])
    for a in tweets_candidat:  #cherche le nombre minimal d'hashtags d'un tweet pour un candidat donné
        len_a=len_hashtag(a)
        if len_a<=min_hashtags:
            min_hashtags=len_a
    return(min_hashtags)
    
def max_hashtag(tweets_candidat):
    """compte le nombre maximal de hashtags par candidat dans un tweet"""
    max_hashtags=len_hashtag(tweets_candidat[0])
    for a in tweets_candidat:  #cherche le nombre maximal d'hashtags d'un tweet pour un candidat donné
        len_a=len_hashtag(a)
        if len_a>=max_hashtags:
            max_hashtags=len_a
    return(max_hashtags)
    
def avg_hastag(tweets_candidat):
    """calcule le nombre moyenne de hashtags des tweets pour un candidat"""
    nombre_tweets=len(tweets_candidat)
    nombre_hashtags=0
    for a in tweets_candidat: #parcourt la liste de tweet pour compter le nombre total de hashtags
        len_a=len_hashtag(a)
        nombre_hashtag+=len_a
    return(nombre_hashtag/nombre_tweets)

def execute(tweets):
    candidats = [] # On renvoie la liste des listes de tweets associés à chaque candidat
    avg_hashtag, max_hashtag, min_hashtag, min_len_tweets, max_len_tweets, avg_len_tweets, min_fav, max_fav, avg_fav, min_RT, max_RT, avg_RT = [], [], [], [], [], [], [], [], [], [], [], []

    for c in range(1, numberCandidates + 1): # On calcule l'ensemble des valeurs associées à l'ensemble des tweets liés à chque candidat
        candidats.append([t for t in tweets if t["candidat"] == c])
        avg_hashtag.append(avg_hashtag(candidats[-1]))
        max_hashtag.append(max_hashtag(candidats[-1]))
        min_hashtag.append(min_hashtag(candidats[-1]))
        max_len_tweets.append(max_len_tweets(candidats[-1]))
        avg_len_tweets.append(avg_len_tweets(candidats[-1]))
        min_fav.append(min_fav(candidats[-1]))
        max_fav.append(max_fav(candidats[-1]))
        avg_fav.append(avg_fav(candidats[-1]))
        min_RT.append(min_RT(candidats[-1]))
        max_RT.append(max_RT(candidats[-1]))
        avg_RT.append(avg_RT(candidats[-1]))

    return {"avg_hashtag" : avg_hashtag, "max_hashtag" : max_hashtag, "min_hashtag" : min_hashtag, "min_len_tweets" : min_len_tweets, "max_len_tweets" : max_len_tweets,"avg_len_tweets" : avg_len_tweets, "min_fav" : min_fav, "max_fav" : max_fav, "avg_fav" : avg_fav, "min_RT" : min_RT, "max_RT" : max_RT, "avg_RT" : avg_RT} 

from textblob import TextBlob
from textblob import word

#on suppose que tweet est la chaine de caractère contennant l'ensemble des tweets


tweets = TextBlob(tweet)


def tweets_lematises(tweets):
    """renvoie la liste des mots lémmatisés pour l'ensemble des tweets"""
    mots_lematises=[]
    tweets=tweets.words
    for words in tweets:
        w=word(words)
        lemma=w.lemmatize()
        mots_lematises.append(lemma)
    return(mots_lematises)
    
def tweets_mots_uniques(tweets):
    """renvoie la liste des mots uniques pour l'ensemble des tweets"""
    mots_unique=[]
    tweets=tweets.words
    for words in tweets:
        if tweets.word_counts[words]==1:
             mots_unique.append(words)
    return(mots_unique)
    


#ici tweet est un tweet en chaine de caractère 


def is_a_neutral_tweet(tweet):
    """Cette fonction booléenne vérifie qu'un tweet est objectif"""
    tweet=TextBlob(tweet)
    polarity=tweet.sentiment.polarity 
    if polarity>=-0,3 and polarity<=0,3
        return True
    return False 
    
def is_a_pos_tweet(tweet):
    """cette fonction booléenne vérifie qu'un tweet est positif"""
    tweet=TextBlob(tweet)
    polarity=tweet.sentiment.polarity 
    if polarity > 0,3:
        return True 
    return False 
    
def is_a_neg_tweet(tweet):
    """cette fonction booléenne vérifie qu'un tweet est négatif"""
    tweet=TextBlob(tweet)
    polarity=tweet.sentiment.polarity 
    if polarity < -0,3:
        return True
    return False

#list_tweets est la liste des tweets pour un candidat donné
    
def list_pos_tweets(list_tweets):
    """renvoie la liste des tweets positifs"""
    list_pos_tweet=[]
    for tweet in list_tweets:
        if is_a_pos_tweet(tweet):
            list_pos_tweet.append(tweet)
    return list_pos_tweet
            
            
def list_neg_tweets(list_tweets):
    """renvoie la liste des tweets negatifs"""
    list_neg_tweet=[]
    for tweet in list_tweets:
        if is_a_neg_tweet(tweet):
            list_neg_tweet.append(tweet)
    return list_neg_tweet
            
            
def list_neutral_tweets(list_tweets):
    """renvoie la liste des tweets neutres"""
    list_neutral_tweet=[]
    for tweet in list_tweets:
        if is_a_neutral_tweet(tweet):
            list_neutral_tweet.append(tweet)
    return list_neutral_tweet
    
list_pos_tweet=list_pos_tweets(list_tweets)
    
list_neg_tweet=list_neg_tweets(list_tweets)

list_neutral_tweet=list_neutral_tweets(list_tweets)

print("Percentage of positive tweets: {}%".format(len(list_pos_tweets)*100/len(list_tweets)))
print("Percentage of neutral tweets: {}%".format(len(list_neutral_tweets)*100/len(list_tweets)))
print("Percentage de negative tweets: {}%".format(len(lits_neg_tweets)*100/len(list_tweets)))

         
