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
