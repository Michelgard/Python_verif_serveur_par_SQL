#!/usr/bin/env python
# -*- coding: utf-8 -*

# on importe le module MySQLdb
import MySQLdb

# modules pour date et heure
import datetime
import time

#module pour mail
import smtplib
from email.mime.text import MIMEText

#Module pour le SSH 
import paramiko

from config import *

# Connexion SSH pour le reboot
def rebootSSH(hostSSH, userSSH, passWordSSH):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostSSH, username=userSSH, password=passWordSSH)
    ssh.exec_command("sudo reboot")

# Envoie mail 
def sendEmail(email_from, email_to, subject, text, smtp, portSmtp, mailLogin, passLogin):
    msg = MIMEText(text)
    msg['Subject'] = subject
    msg['From']    = email_from
    msg['To']      = email_to
    s = smtplib.SMTP(smtp, portSmtp)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(mailLogin, passLogin)
    s.sendmail(email_from,[email_to],msg.as_string())
    s.quit()

def connexSQL(paramMysql, sql, colonne):
    try:
        # On  créé une conexion MySQL
        conn = MySQLdb.connect(**paramMysql)
        # On créé un curseur MySQL
        cur = conn.cursor(MySQLdb.cursors.DictCursor)
        # On exécute la requête SQL
        cur.execute(sql)
        # On récupère toutes les lignes du résultat de la requête
        rows = cur.fetchall()
        # On parcourt toutes les lignes
        for row in rows:
            # Pour récupérer les différentes valeurs des différents champs
            dateDerniere = row[colonne]
            return dateDerniere
				
    except MySQLdb.Error, e:
        # En cas d'anomalie
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:
        # On ferme la connexion
        if conn:
            conn.close()

# On recupère l'heure de la derniere donnée entrée dans la table
dateDerniere = connexSQL(paramMysql, sql, colonne)

#Date et heure maintenant
deSuite = datetime.datetime.now() 
#calcul du delta pour savoir si le serveur envoi toujours des données
delta = datetime.timedelta(minutes=delais)
   
#On compare le temps si desuite est < a la dernière valeur de la base ou pas
if deSuite < (dateDerniere + delta):
    if mailOK:
        sendEmail(email_from, email_to, sujetMailOK, texteMailOK, smtp, portSmtp, 
		    mailLogin, passLogin)
else:
    if mailNonOK:
        sendEmail(email_from, email_to, sujetMailNonOK, texteMailNonOK, smtp, 
		    portSmtp, mailLogin, passLogin)
    #reboot du serveur si une erreur est détectée
    rebootSSH(**paramSSH)


