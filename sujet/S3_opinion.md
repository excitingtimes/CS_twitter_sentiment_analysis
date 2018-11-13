# Fonctionnalité 9 : Prise en compte de l'opinion


A l'aide de Textblob, écrivez le code nécessaire à l'analyse de l'opinion pour un candidat donné. Votre code devrait vous permettre de pouvoir mettre en oeuvre ce type d'instructions :

```PYTHON

print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['tweet_textual_content'])))
print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['tweet_textual_content'])))
print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['tweet_textual_content'])))
```



**Pensez à tester et à documenter votre code !!!**

ET :

+ <span style='color:blue'>Faire un commit.</span> 
+ <span style='color:blue'>Pousser (Push) votre code vers votre dépôt distant sur GitLab.</span> 

Et nous arrivons à la fin de notre MVP la [**Fonctionnalité 10** : Afficher le résultat de l'analyse.](./S4_displayresult.md)