# TwitterPredictor - Sprint 0 : Analyse du problème

Une des premières étapes de tout travail de programmation et de développement logiciel, quelque soit la méthodologie de développement utilisée, consiste à réaliser une rapide **analyse des besoins**, avant toute phase d'implémentation.

Cette analyse a pour objectif d'identifier les principales fonctionnalités à developper pour avoir le comportement souhaité du système développé. Cette première liste de fonctionnalité n'a pas besoin d'être exhaustive ni figée mais elle vous permettra de construire vos premiers developpements.


## Analyse des besoins : les principales fonctionnalités

L'objectif ici est de pouvoir prédire, à partir d'un ensemble de tweets relatifs à une élection, de pouvoir prédire le résultat de cette dernière à partir de l'analyse de leur opinion.

Le **[MVP (Minimum Viable product)](https://medium.com/creative-wallonia-engine/un-mvp-nest-pas-une-version-simplifi%C3%A9e-de-votre-produit-89017ac748b0)** de ce projet consistera à livrer une première version de l'outil d'analyse de bout en bout, c'est-à-dire de la collecte à la prédiction et sa visualisation avec des solutions simples.

En particulier, le MVP : 

+ **Permettra de se connecter à l'API Twitter pour collecter un ensemble de tweets relatifs à une élection**.
+  **Se basera uniquement sur l'analyse du contenu textuel des tweets et négligera l'information sur l'auteur du tweet, son type (*retweet*, *reply*,...) et son contenu multimédia**.
+ **Permettra un traitement et une analyse simples des tweets.**
+ **Affichera les résultats de l'analyse sous la forme d'un graphe temporel comme ci-dessus.**

 
D'autres fonctionnalités pourront bien sûr être ajoutées ensuite pour améliorer votre projet après avoir fini ce MVP mais en construisant une chaîne de bout en bout, vous pourrez rapidement avoir des retours sur votre produit et ses fonctionnalités.

Vous pouvez maintenant continuez par le [Sprint 0 : Reflexion autour de la conception](./Sprint0Conception.md).