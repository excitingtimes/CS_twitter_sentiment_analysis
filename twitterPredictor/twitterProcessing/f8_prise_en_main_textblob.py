from textblob import TextBlob
from textblob import word

#on suppose que tweet est la chaine de caractère contennant l'ensemble des tweets


tweets = TextBlob(tweet)


def tweets_lematises(tweets):
    """renvoie la liste des mots lémmatisés pour l'ensemble des tweets"""
    mots_lematises=[]
    for words in tweets:
        w=word(words)
        lemma=w.lemmatize()
        mots_lematises;append(lemma)
    return(mots_lematises
    
def tweets_mots_uniques(tweets):
    """renvoie la liste des mots uniques pour l'ensemble des tweets"""
    mots_unique=[]
    for words in tweets:
        if tweet.word_counts[words]==1:
            mots_unique.append(words)
    return(mots_unique)
    
        
