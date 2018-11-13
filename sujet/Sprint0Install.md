# TwitterPredictor - Sprint 0 : Installation du socle technique


Le premier travail consiste à préparer le socle technique nécessaire au bon developpement du projet. Le projet **twitterPredictor** sera :

+ Un projet Pycharm 
+ Utilisant [git](https://git-scm.com/) comme gestionnaire de version
+ Qui sera déposé sur le [GitLab pédagogique de CentraleSupélec](https://gitlab-student.centralesupelec.fr/).

## Créer un projet Pycharm : **`twitterPredictor`**

Si ce n'est pas déjà fait, [créer un projet Pycharm](./pycharm.md) que vous appelerez **`twitterPredictor`** puis ajouter un package de nom **twitterPredictor** au projet. Un fichier `__init__.py` vide est automatiquement ajouté au package. 

## Versionner avec git

### Mise en place de Git sur le projet **`twitterPredictor`**

Comme vous devrez apprendre à le faire de manière systématique pour tout travail de développement informatique à plusieurs, vous devez passer le projet **`twitterPredictor`** sous Git.


Pour commencer, et pour comprendre git, faites le rapide tutorial disponible [ici](http://rogerdudler.github.io/git-guide/index.fr.html). 
D'autres tutoriaux très bien:
 
 + [http://marklodato.github.io/visual-git-guide/index-en.html](http://marklodato.github.io/visual-git-guide/index-en.html)
 + [https://openclassrooms.com/fr/courses/1233741-gerez-vos-codes-source-avec-git](https://openclassrooms.com/fr/courses/1233741-gerez-vos-codes-source-avec-git)
 + ...


Ensuite nous allons mettre en place un dépôt git pour notre projet.





+ Depuis Pycharm, vous pouvez le faire depuis le menu **(`VCS | Enable Version Control Integration`)**.
+ Faire un premier `commit`contenant le fichier `__init__.py`
+  Créer un dépôt **`twitterPredictor`** sur GitLab qui vous servira de **depôt distant**.
+  Connecter votre dépôt distant à votre dépôt local. Pour cela, vous pouvez :
	+ soit le faire en ligne de commande
			`git remote add nom_local_du_dépôt_distant url `
	+  soit utiliser et configurer  correctement la commande `Push` disponible dans le menu **(`VCS | Git | Push`)**

+ Se rendre sur le dépôt distant (**sur GitLab**) pour :
	+ Vérifier que l'opération `Push` a été effectuée correctement
	+ Créer depuis GitLab un fichier `README.md`. Vous pouvez vous inspirer de ce [template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) pour avoir une idée de ce que votre README devrait contenir. Pour commencer, vous vous contenterez de donner un titre à votre projet et d'y ajouter une petite description.
	+ Commiter l'ajout de ce `README.md`.
	
+ Il faut maintenant mettre à jour votre dépôt local. Pour cela il faudra revenir dans Pycharm et configurer l'option `Fetch` dans le menu **(`VCS | Git | Fetch`)**.
+ Procéder à un `Fetch`.
+ Procéder à un `Merge` pour que les données rapatriées puissent fusionner avec les données locales. Votre fichier `README.md` devrait apparaître dans votre IDE.


Votre projet  **`twitterPredictor`** est prêt pour la suite.


### Ajout de collaborateurs

Vous allez maintenant ajouter votre binôme et votre enseignant comme collaborateir de votre dépôt. Pour cela, allez sur votre depôt GitLab et choisissez le menu `Settings | Members` dans la fenêtre de gauche. Ajouter votre binôme et votre enseignant comme collaborateur. Votre binôme sera *Developer* et votre enseignant sera *Reporter*.


## Déposer sur GitLab

Il vous sera demandé plusieurs fois le long du projet et des séances de pousser votre code sur le dépôt distant. 

Pour ceux d'entre vous qui débutent, il serait plus facile de se contenter au début de suivre un workflow classique sans branches, avec des `commit` sur la branche principale `master`chaque fois que cela vous est demandé et systématiquement en fin de séance. Pour ceux d'entre vous qui sont déjà très familiarisés avec git, vous savez que la démarche plus classique consiste à développer une branche par fonctionnalité et à fusionner ensuite dans la branche `master`.

Nous allons procéder comme suit pour le projet :

+ Vous aurez un dépôt distant commun pour le binôme.
+ Chaque membre du binôme construira une branche qui lui sera proche.

```
 git checkout -b projet_membre_x
 git push origin projet_membre_x
```
 
 
 + A chaque fois que vous terminerez une fonctionnalité, vous procederez alors à un `merge request` avec la commande

 `git merge <branch>`
 
 + Il vous faudra donc pour ne pas avoir trop de problèmes sur cette opération, vous mettre d'accord sur votre code (en faisant une sorte de cycle de [pair programming](pair programming))
 



Vous pouvez maintenant continuez par le [Sprint 0 : Analyse du problème](./Sprint0Analyse.md).