# Fonctionnalité 3 : Collecter des tweets relatifs à une élection


L'objectif de cette fonctionnalité est la mise en oeuvre effective de la collecte de tweets et la réalisation de cette collecte sur un instance du problème. Comme nous ne sommes pas en période électorale en France, vous allez instancier votre projet à une **analyse d'opinions sur deux personnalités (politiques) françaises qui ont une actualité la semaine prochaine**. On peut par exemple, prendre Emmanuel Macron et Edouard Philippe pour comparer l'opinion de la sphère sociale entre le président et le premier ministre mais vous pouvez aussi choisir d'autres personnalités, politiques ou non mais qui ont une actualité  cette semaine.


## Etape 1 : Définir un ensemble de mots clés pour la collecte de tweets par l'API `search` et créer les requêtes associées.

Un premier travail pour initier la collecte est de définir l'ensemble des mots clés que vous allez utiliser pour votre collecte via l'API `search`. Nous allons considérer que cette liste de mots clés vous est fournie par votre *client* sous la forme de fichiers `keywords_candidate_n.txt` avec un mot clé (ou un ensemble de mots clés) par ligne. De la même manière, votre *client* vous fournira une liste de `hashtag_candidate_n.txt` qui sont les hastags associés à chaque candidat. 
Ces fichiers seront stockés dans un répertoire `CandidateData` à la racine de votre projet. 

Il s'agit maintennant d'écrire une fonction `get_candidate_queries(num_candidate,file_path)` qui permet de créer et de renvoyer un ensemble de requêtes destinées à l'API `search` pour le candidat `num_candidate` à partir des fichiers `keywords_candidate_num_candidate.txt` et `hastag_candidate_num_candidate.txt`.

Pour cela il est intéressant de bien connaître les bonnes pratiques d'utilisation de cette API, décrites [ici](https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators.html).

N'oubliez pas les commentaires ! Ainsi le début de votre fonction devrait ressembler à cela :

```PYTHON
def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag 
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        # TO COMPLETE
    except IOError:
        # TO COMPLETE

```


**N'oubliez d'ajouter des tests unitaires à votre projet avec pytest.**


## Etape 2 : Collecter les tweets via l'API `Search`

Nous pouvons maintenant, dans le module `collect_candidate_actuality_tweets`,  écrire la fonction `get_tweets_from_candidates_search_queries(queries, twitter_api)` qui étant donnée une liste `queries` de requêtes (de type `search`) et une instance de connexion `twitter_api` récupére et renvoie les tweets répondant aux différentes requêtes.
Il faudra bien faire attention à prendre en compte les [différents types d'erreurs](http://docs.tweepy.org/en/v3.6.0/api.html#tweepy-error-exceptions) pouvant se produire lors de la collecte.


## Etape 3 : Collecter les tweets qui sont une réponse à un tweet d'un candidat donné.

Pour notre application d'analyse de l'opinion sociale sur un candidat, il peut être intéressant de récupérer et d'analyser les réponses à un tweet du candidat en question.

Ajouter au module `collect_tweet_candidate_activity` une fonction `get_replies_to_candidate(num_candidate)` qui permet de renvoyer pour chaque tweet recent d'un candidat donné, les réponses à ce tweet. On conservera dans le type de retour l'information sur le tweet d'origine.
 
<span style='color:red'>Commenter et tester votre code !</span>

## Etape 4 : Collecter les tweets retweets d'un candidat donné

Pour analyser l'évolution de l'opinion sur un candidat donné, une métrique interessante peut-être de regarder le nombre de retweets des tweets d'un candidat donné.

Ajouter au module `collect_tweet_candidate_activity` une fonction `get_retweets_of_candidate(num_candidate)` qui permet de renvoyer pour chaque tweet recent d'un candidat donné, les re-tweets à ce tweet. On conservera dans le type de retour l'information sur le tweet d'origine.

<span style='color:red'>Commenter et tester votre code !</span>

## Etape 5 : Collecter le flux de tweets à propos d'un candidat.

Nous voulons maintenant capter ce qui se dit en temps réél sur un candidat donné sur la sphère Twitter ainsi que l'activité du candidat sur cette sphère et ce qu'elle engendre comme réponse. A partir de l'API `Streaming and Filter` mettez en place un mécanisme d'écoute et de capture des tweets relatifs à un candidat donné en continu ainsi que des tweets en réponse à un tweet d'un candidat donné.

<span style='color:red'>Commenter et tester votre code !</span>

## Etape 6  : Mise en orchestre de la collecte

Nous arrivons bientôt au terme de notre fonctionnalité. Il s'agit maintenant de mettre toutes les fonctions précédentes en orchestre au sein d'une fonction principale. Vous ajouterez donc un fichier `__main__.py` au package `tweet_collection` dans lequel vous ecrirez votre programme principal initiant et executant une collecte.


Nous avons fini cette fonctionnalité donc n'oubliez pas de : 

+ <span style='color:blue'>Faire un commit sur votre dépôt local.</span> 
+ <span style='color:blue'>Pousser (Push) votre code vers votre dépôt distant sur GitLab.</span> 


Nous pouvons maintenant passer à la [**Fonctionnalité 4** : Stocker les tweets.](./S1_twitterstorage.md)














