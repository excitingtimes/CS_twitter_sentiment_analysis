import tweepy

from credentials import *
from tweepy.streaming import StreamListener

count = 100

def twitter_setup():
    # Cette fonction permet d'établir un lien avec l'API Tweeter. Elle renvoie un objet de type API si la connexion est un succès, None sinon 

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) # Authentification
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)

    return api



def collect(query, count):
    # Cette fonction renvoie les résultats d'une requête telle que entrée dans la barre de recherche de Tweeter, et filtre le résultat suivant le nombre de lignes désiré

    connexion = twitter_setup() # Mise en place d'une connexion avec l'API
    tweets = connexion.search(q = query, rpp = count)

    return tweets



def collect_by_user(user_id, count = 200):
    # Cette fonction affiche les éléments figurants dans la timeline d'un utilisateur tweeter

    connexion = twitter_setup() # Mise en place d'une connexion avec l'API
    statuses = connexion.user_timeline(user_id, count)

    return statuses



class StdOutListener(StreamListener): # Classe permettant l'écoute continue d'un stream de tweets
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True

def collect_by_streaming(terms_to_track):
    # Fonction permettant d'écouter un flux de tweets correspondant à un certain critère

    connexion = twitter_setup() # Mise en place d'une connexion avec l'API
    listener = StdOutListener() # Écoute du flux de streams

    stream=tweepy.Stream(auth = connexion.auth, listener=listener) # Connexion au stream
    stream.filter(track = terms_to_track)



def get_candidate_queries(num_candidate=1, file_path="../../inputData/"):
    # Fonction permettant d'obtenir une liste de requêtes à partir de mots-clés et de hashtags concernant un candidat politique

    keywordsPath = file_path + "keywords" + str(num_candidate) + ".txt"
    hashtagsPath = file_path + "hashtags" + str(num_candidate) + ".txt"

    keywordsFile = open(keywordsPath, "r")
    hashtagsFile = open(hashtagsPath, "r")
    
    keywords = keywordsFile.readlines() # On obtient une liste de mots - clés (et des hashtags)
    hashtags = hashtagsFile.readlines()

    for k in keywords : # On nettoie les données au préalable
	k.trim()
	k.toLowerCase()

    for h in hashtags:
	h.trim()
	h.toLowerCase()

    keywordsFile.close()
    hashtagsFile.close()   
    
    try: # on concatène les deux listes de requêtes
        queries = keywords + hashtags
	return queries
    except IOError:
       return []

def get_tweets_from_candidates_search_queries(queries, twitter_api):
    # Fonction permettant de concaténer les tweets renvoyés pour chaque requête sur l'API twitter fournie en argument 
    result = []
	
    for query in queries : # Pour chaque requête, on ajoute au résultat final le résultat de l'appel à l'API
        result += twitter_api.search(q = query, rpp = count)
	
        return result

def get_replies_to_candidate(num_candidate, idTweet):
    # Fonction retournant pour l'id du tweet passé en paramètre l'ensemlbe de ses réponses

    
    
def get_retweets_of_candidate(num_candidate, idTweet):
    # Fonction retournant pour l'id du tweet passé en paramètre l'ensemble de ses retweets
