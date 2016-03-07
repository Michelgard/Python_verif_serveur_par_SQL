# -*- coding: utf-8 -*

# On créé un dictionnaire contenant les paramètres de connexion MySQL
paramMysql = {
    'host'   : 'localhost',
    'user'   : 'user base',
    'passwd' : 'pass word base',
    'db'     : 'Nom base'
}
# Bien respecter les noms des paramètres (host, user, passwd, db)


#Requete SQL pour vérifier la dernière donnée d'une table
sql = """\
SELECT * FROM Temp_Salon 
WHERE ID_Temp_Salon = (  SELECT MAX( ID_Temp_Salon )  
FROM Temp_Salon )
"""

#colonne heuretime de la base 
colonne = 'Date_Temp_Salon'

#Données pour le mail
smtp = 'smtp.gmail.com'
portSmtp = 587
mailLogin = 'xxxxxx@gmail.com'
passLogin = 'pass login mail'
email_from = 'xxxx@gmail.com'
email_to = 'xxxxxxxx@gmail.com'

mailOK = True
sujetMailOK = 'Connexion serveur OK'
texteMailOK = 'Tout va bien !'

mailNonOK = True
sujetMailNonOK = 'Erreur Connexion serveur'
texteMailNonOK ='Erreur sur la base. Reboot du serveur'

#Delais maximun entre deux enregistrements
delais = 20

#Données pour la connexion SSH
paramSSH = {
    'hostSSH'   		: 'ip servuer ssh',
    'userSSH'   		: 'user SSH',
    'passWordSSH' 	: 'pass SSH'
}
    
