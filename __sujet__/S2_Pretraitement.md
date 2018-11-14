# Fonctionnalité 5 - Quelques informations statistiques

L'objectif ici est de tirer parti des dataframes pandas pour faire des premières analyses statistiques et obtenir des premières informations sur les tweets collectés.

Ici, il peut être nécessaire de refaire une étape de conception avec l'ensemble de parties prenantes pour être certains d'extraire les bonnes informations.


Supposons que dans l'étape précédente, nous ayons récupéré nos tweets sous la forme d'un dataframe comme ci-dessous :


```
                               tweet_textual_content  len  ...   Likes   RTs
0  RT @EmmanuelMacron: Old demons are rising agai...  140  ...       0  4233
1            @1tortuerouge @EmmanuelMacron D’accord.   39  ...       0     0
2  RT @lesRepublicains: 🌱 « C'est de l'écologie, ...  140  ...       0    34
3  RT @LivelyLoyce: #IGF2018  Hate speech and onl...  140  ...       0     6
4  RT @LydiaGuirous: Erdogan n’a pas sa place à l...  140  ...       0  1103
5  RT @FLOTUS: Thank you @EmmanuelMacron and Mrs....  140  ...       0  4989
6  @Europe1 Rien ne sert de recruter s'ils se don...  140  ...       0     0
7  @JustinTrudeau @EmmanuelMacron Thank you for c...  144  ...       0     0
8  RT @jtmetrop: @EmmanuelMacron ne sent pas la c...   96  ...       0     1
9  RT @SecPompeo: It is a humble honor to join @P...  139  ...       0  2681
```
On a donc les colonnes `tweet_textual_content`, `len`, `ID`, ..., `Likes` et `RTS`.

On peut par exemple, extraire le tweet qui a le plus de mention de `retweet` de la manière suivante :


```PYTHON
rt_max  = np.max(data['RTs'])
rt  = data[data.RTs == rt_max].index[0]

# Max RTs:
print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data['len'][rt]))
```
Ce qui donne dans mon cas ici :

```
The tweet with more retweets is: 
RT @EmmanuelMacron: Patriotism is the exact opposite of nationalism. Nationalism is a betrayal of patriotism. By putting our own interests…
Number of retweets: 72043
139 characters.

```

Placer vous ou créer un package `tweet_analysis` à votre projet et concever et programmer un ensemble de fonctions permettant d'extraire des informations pertinentes d'un ensemble de tweets.


## A Faire

+ <span style='color:blue'>Faire un commit dès que la réalisation de la  fonctionnalité ou d'une sous-fonctionnalité est finie.</span> 
+ <span style='color:blue'>Pousser (Push) votre code vers votre dépôt distant sur GitLab.</span> 


Nous pouvons maintenant passer à la fonctionnalité [**Fonctionnalité 6** : Visualisation de l'évolution d'une caractéristique.](./S2_TweetTimeSeries.md)


 

