import tweepy

from credentials import *
from tweepy.streaming import StreamListener



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

