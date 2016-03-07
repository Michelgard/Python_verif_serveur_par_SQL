# Python_verif_serveur_par_SQL
Code Python pour vérifier le fonctionnement de SQL sur un serveur

A la maison j'ai un Raspberry Pi qui avec une tache cron envoi des valeurs de température dans une base de données sur un serveur VPS.

J'ai intallé une verification sur le Raspberry Pi pour la connexion internet. Si la connexion est perdu plus de 5 minutes il reboot.
Mais il arrive que la connexion soit bonne mais qu'aucune info ne soit envoyée sur la base SQL du serveur VPS distant.

Donc j'ai fait ce code en Python.
Dans un premier temps il récupère la dernière valeur dans une table de la base des températures. Il faut que cette valeur soit enregistrée avec une colonne DateTime pour récupérer l'heure de la dernière entrée.
Ensuite on ajoute un delta. Dans mon cas les infos arrivent dans la table toutes les 5 minutes donc j'ajoute 20 mn et si avec cette heure je suis inférieur à l'heure actuelle c'st qu'il y a un problème sur le Raspberry.

J'ai ajouté la possibilité d'envoyer un mail quand tout va bien et quand quelque chose ne marche pas.

Et bien sur si cela ne va pas il y a un reboot du Raspberry Pi par une connexion SSH.

Pour l'utilisation il faut entrèe les host, login et mots de passe pour La connexion à la base de données, le mail et le SSH.

Pour les retours raspberrypi.gard@gmail.com.

