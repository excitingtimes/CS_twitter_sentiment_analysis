# Fonctionnalité 2 : Collecter des tweets avec Tweepy - Prise en main

Maintenant que nous avons établi une connexion avec l'API Twitter, nous allons utiliser cette connexion pour collecter des tweets. En particulier, avec les APIs de Twitter nous pouvons :

+ recupérer des tweets historiques (de 7 jours précédents) à l'aide de mots clés (`API Search`)
+ récupérer les tweets et l'activité d'un utilisateur donné (`API Users`)
+ capter et filtrer un flux de tweets en temps réel (`API Streaming and Filter`)


Attention, l'accès à ces différentes APIs est limité. Les règles sont [ici](https://developer.twitter.com/en/docs/basics/rate-limiting.html). 


## Etape 1 : Prise en main de l'API [Search](https://developer.twitter.com/en/docs/tweets/search/overview)

Nous allons ici prendre en main l'API `Search` à l'aide de Tweepy. Rappelez-vous que l'utilisation aux APIs de Twitter est limitée et prenez donc le temps de bien reflechir à ce que vous faites.


La documentation générale de ce que permet Tweepy est disponible [ici](http://docs.tweepy.org/en/v3.6.0/api.html).

Voici en particulier la documentation de la fonction `search`.

```
API.search(q[, lang][, locale][, rpp][, page][, since_id][, geocode][, show_user])
```

qui renvoie les tweets qui sont en correspondance avec la requête `q`

avec les paramètres suivants:	

+ `q` – the search query string
+ `lang` – Restricts tweets to the given language, given by an ISO 639-1 code.
+ `locale` – Specify the language of the query you are sending. This is intended for language-specific clients and the default should work in the majority of cases.
+ `rpp` – The number of tweets to return per page, up to a max of 100.
+ `page` – The page number (starting at 1) to return, up to a max of roughly 1500 results (based on rpp * page.
+ `since_id` – Returns only statuses with an ID greater than (that is, more recent than) the specified ID.
+ `geocode` – Returns tweets by users located + `show_user` – When true, prepends “<user>:” to the beginning of the tweet. This is useful for readers that do not display Atom’s author field. The default is false.


Que fait le code  ci-dessous ?

``` PYTHON
def collect():
    connexion = connect.twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)
```

Recopier le et faites les adaptations nécessaires et prenez le temps de jouer un peu avec les différents paramètres de cette fonction `search` pour vous familiarisez avec.

En particulier, vous pouvez tester avec les requêtes suivantes :

```
"Emmanuel Macron"
"Emmanuel and Macron"
"Emmanuel AND Macron"
"Emmanuel OR Macron"
"Emmanuel -Macron"
"#EmmanuelMacron"
"@EmmanuelMacron"

```

Prenez le temps de regarder la richesse de ce qui est renvoyé. Une descriptif est fourni [ici](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object).




## Etape 2 : Prise en main de l'API [Users](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/overview)

Cette API de Twitter permet de récupérer des données sur les utilisateurs et notamment leurs tweets, leurs tweets re-tweetés... 

Tweepy fournit un ensemble de méthodes pour s'interfacer avec cette API et il vous est donc conseillé de vous référer à la documentation [ici](http://docs.tweepy.org/en/v3.6.0/api.html?highlight=user_timeline)

Que fait le code  ci-dessous ?

```PYTHON
def collect_by_user(user_id):
    connexion = connect.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return statuses
```

Recopier le et faites les adaptations nécessaires et prenez le temps de jouer un peu avec les différents fonctions de cette API pour vous familiarisez avec.


## Etape 3 : Prise en main de l'API [Streaming](https://developer.twitter.com/en/docs/tweets/filter-realtime/overview)


Cette API permet de récupérer des twweets en continu avec d'éventuelles opérations de filtrage. Tweepy a aussi des outils pour permettre l'accès à cette API. Une documentation est disponible [ici](http://docs.tweepy.org/en/v3.6.0/streaming_how_to.html?highlight=streaming).


```PYTHON
from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):

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




def collect_by_streaming():

    connexion = connect.twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=['Emmanuel Macron'])
```

Recopiez et testez le code ci-dessus. Que fait-il ? Attention, vous faites du streaming donc il faudra bien penser à interrompre votre captation.

Cette API est intéressante pour faire de la captation de flux Twitter. Elle est cependant assez délicate à manipuler. Vous avez sur cette [page](https://www.programcreek.com/python/example/86213/tweepy.Stream) un ensemble d'exemples d'utilisation de cette API (attention parfois en python 2). 


## Etape 4 : Initier un module de collecte pour notre application


Maintenant que vous avez fait un rapide tour des possibilités de Tweepy pour collecter des tweets depuis l'API de Twitter, revenons à notre problème. Nous voulons collecter des tweets relatif à un évènement donné, une élection dans notre cas, de la manière la plus exhaustive possible.

Nous avons donc une **élection** qui est un évènement qui oppose à minima deux **candidats** l'un contre l'autre. 

Pour ce projet, on considèrera que l'**élection** est un évènement d'actualité et que la collecte avec l'`API Search` qui ne permet de récupérer que les tweets des 7 jours précédents est suffisante. Pour ce projet, pour le simplifier, on supposera aussi que l'évènement est suffisamment important pour considérer que tous les tweets évoquant d'une manière ou une autre au moins l'un des candidats (vocabulaire relatif au candidat, son parti, les [hashtags](https://fr.wikipedia.org/wiki/Hashtag) associés...) est représentatif et important pour notre analyse d'opinions. Une partie de notre collecte consistera donc en la récupération de l'ensemble des tweets relatifs aux différents candidats dont ils ne sont pas auteurs.


De même, la notion de **candidats** est importante pour notre collecte et il pourra par exemple être intéressant de capter l'ensemble des *retweets* d'un tweet d'un candidat ou d'un membre de son équipe ou l'ensemble des *reply* d'un tweet du candidat ou d'un membre de son équipe. 

Enfin, il peut être intéressant de capter en temps réel ce qui est dit sur un candidat donné ou un membre de son équipe.

En prenant en compte ce petit cahier des charges, ajouter les modules `tweet_collect_whole`, `collect_candidate_actuality_tweets` et `collect_candidate_tweet_activity` à votre package `tweet_collection` et essayer de mettre en place une stratégie de collecte des tweets relatifs à une election.

Il s'agit ici, étant donnés ces 3 modules, d'identifier les principaux objets nécessaire pour la mise en place de votre collecte et de réfléchir à l'orchestration des différentes méthodes de collecte mais pas d'implémenter cela, ce qui est l'objet de la prochaine fonctionnalité (**Fonctionnalité 3** : Collecter des tweets relatifs à une election).


Dans l'établissement de votre stratégie, pour pourrez prendre en compte


Discutez en binôme ou en groupe de cette fonctionnalité, schématiser, spécifier et comme précédemment, prenez une photo de ce travail de conception et <span style='color:blue'> déposer ce travail dans le  `WorkingDocs`de votre dépôt git. N'oubliez pas de faire un `commit` et de mettre à jour votre dépôt distant.</span>



Nus pouvons maintenant passer à la [**Fonctionnalité 3** : Collecter des tweets relatifs à une élection.](./S1_twittercollectquery.md)





















