# Fonctionnalité 1 : Prise en main de tweepy - Se connecter à l'API Twitter


Pour pouvoir faire ce projet, il est nécéssaire de collecter l'ensemble des tweets relatifs à une élection (ou au mieux un ensemble de tweets représentatifs). 

Pour se faire, Twitter a mis à la disposition de tous un ensemble d'[API](https://fr.wikipedia.org/wiki/Interface_de_programmation)s permettant un accès programmatique à ses données. Vous avez vu le concept d'APis dans le cours de SIP mais si quelques révisions sont nécessaires, vous pouvez consultez le cours d'OpenClassRooms sur les [APIs REST](https://openclassrooms.com/fr/courses/3449001-utilisez-des-api-rest-dans-vos-projets-web). La [vidéo](https://www.lewagon.com/fr/blog/api-webhook-debutant-tutoriel) du tutorial de S. Saunier du Wagon est aussi une très bonne introduction pour les débutants.

Les APIs Twitter sont nombreuses et très bien décrites [ici](https://developer.twitter.com/en/docs.html). Celle qui nous intéresse particulièrement ici est l'API [**Search**](https://developer.twitter.com/en/docs/tweets/search/overview) qui permet de récupérer des tweets historiques à partir de mots clés. Twitter a recemment revu sa politique de mise à disposition de ses données et de facturation de cette dernière et la recherche se limite maintenant à 7 jours précédents la recherche.

De nombreux outils ont été développés pour faciliter l'utilisation de ces APIs et notamment en python, plusieurs biblithèques sont disponibles :

+ [tweepy](http://www.tweepy.org/)
+ [python_tweeter](https://github.com/bear/python-twitter)
+ [twython](https://github.com/ryanmcgrath/twython )
+ ...

Dans ce projet, nous allons utiliser Tweepy qui est une des bibliothèques qui permet d'accéder relativement facilement aux APIS twitter. La première chose à faire est donc d'installer tweepy soit via PyCharmEdu soit en ligne de commande via la commande:

`pip install tweepy`


Vous pouvez tester l'installation en exécutant l'instruction `import tweepy` sur votre interpréteur python. 

## Etape 1 : se créer un compte twitter.

La première étape pour cette fonctionnalité est de se créer un compte Twitter si vous n'en avez pas car il est nécessaire pour pouvoir avoir accès à l'API.

Après avoir créé votre compte, il est nécessaire d'aller sur le [portail de gestion des applications](https://developer.twitter.com/en/apps) pour créer une `app`. A nouveau, on rentre ici dans un processus assez long (un questionnaire avec pas mal de champ à compléter) qui passe par le dépôt d'une demande de candidature pour avoir un compte `developper` et avoir accès au [portail developper](developer.twitter.com.)

Une fois là, vous pouvez maintenant créer une `app` en complétant encore une fois l'ensemble des informations demandées.

Après cette étape, vous pouvez maintenant récupérer vos `Consumer API keys` et `Access token & access token secret` nécéssaires pour se connecter.

Vous sauverez les différentes valeurs de :

+ Consumer Key (API Key)
+ Consumer Secret (API Secret)
+ Access Token
+ Access Token Secret

dans un fichier `credentials.py` dont le squellette pourrait être le suivant :

```PYTHON
# Twitter App access keys for @user

# Consume:
CONSUMER_KEY    = ''
CONSUMER_SECRET = ''

# Access:
ACCESS_TOKEN  = ''
ACCESS_SECRET = ''

```

**<span style='color:red'> Attention, ce fichier ne sera jamais mis sur votre dépôt git (ni local, et surtout pas distant)</span>**


## Etape 2 : le Hello Word de Tweepy

Vous pouvez maintenant faire le *Hello World* de Tweepy qui consiste en une fonction d'initialisation de l'API Twitter.

```PYTHON
import tweepy
# We import our access keys:
from tweet_collection.credentials import *   

def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

```

Sur cette base, nous allons maintenant initialiser notre module de collecte de tweets. Ajouter à votre projet un package nommé `twitter_collect`. Si vous le faites directement avec PyCharm Edu, vous devriez avoir automatiquement la création d'un fichier `__init__.py` dans le répertoire correspondant à votre package. Dans le cas contraire, vous devez ajouter manuellement ce fichier à votre répertoire pour en faire un package python.

Au passage, voici un petit rappel sur les [modules et les packages](https://docs.python.org/fr/3/tutorial/modules.html) en python.


Dans le package `twitter_collect`, ajouter un module `twitter_connection_setup` (un fichier `twitter_connection_setup.py`) dans lequel vous écrirez donc les fonctions nécessaires pour une connexion à l'API Twitter.




A l'aide de `pytest`, **tester**  votre fonction de connexion à l'API ! Nous verrons plus tard une méthode de developpement appelée **Test Driven Development** qui consiste à écrire les tests avant les fonctions ou autres objets de votre programme mais en attendant, prenez le temps d'ajouter les tests permettant de tester les différentes fonctionnalités de votre projet. 

Ici par exemple, il s'agit d'ajouter un module `test_monmodule.py` à votre projet et de tester que la fonction de connexion à l'API vous renvoit bien un objet non nul.


Nous avons fini ici la fonctionnalité 1. Avant de passer à la fonctionnalité suivante, il vous est demandé de :


+ <span style='color:blue'>Ajouter votre fichier à votre dépôt git.</span>
+ <span style='color:blue'>Faire un commit</span>
+ <span style='color:blue'>Pousser (Push) votre code vers votre dépôt distant sur GitLab.</span> 



## Un peu de prise de recul

Vous avez peut-être trouvé cette première étape assez pénible et avec de nombreuses étapes de création de comptes et d'engagement, beaucoup de formulaires assez détaillés à remplir ... Pour éviter ces étapes, une alternative aurait été de vous founir un jeu de données et de vous faire travailler directement sur ce jeu de données.

Cependant, replaçons nous dans un contexte où vous seriez mandatés par un parti politique pour faire ce travail et même dans le cadre où vous pouvez avoir plusieurs clients qui sont des partis politiques différents. Comment cela aurait impacté cette étape ? Il pourrait, par exemple, être utile de définir la notion d'utilisateur et de prendre cela comme un paramètre de votre utilitaire de connexion à l'API Twitter.

Plus globalement, que sommes-nous en train de faire ? Certaines [actualités récentes](https://www.lemonde.fr/pixels/video/2018/04/14/comment-facebook-peut-il-influencer-le-resultat-d-une-election_5285587_4408996.html), les [scandales](https://www.sciencesetavenir.fr/high-tech/election-de-trump-facebook-bloque-cambridge-analytica_122162) autour de la société Cambridge Analytica, le [RGPD](https://fr.wikipedia.org/wiki/R%C3%A8glement_g%C3%A9n%C3%A9ral_sur_la_protection_des_donn%C3%A9es)... devraient vous permettre de comprendre pourquoi l'accès à ce type de données devient de plus en plus controlé.

Prenez donc le temps de lire rapidement les [règles et les politiques](https://help.twitter.com/fr/rules-and-policies/twitter-api) d'accès aux données de Twitter.



Nous pouvons maintenant passer à la [**Fonctionnalité 2** : Collecter des tweets](./S1_twittercollect.md) pour la collecte des données en elles-mêmes.

