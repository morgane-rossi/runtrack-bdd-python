import mysql.connector
from os import getenv
from dotenv import load_dotenv

load_dotenv()
username = getenv("USERNAME")
userpass = getenv("PASS")

class Employe:
    def __init__(self, id_employe, nom, prenom, salaire, id_service):
        self.id_employe = id_employe
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service

    def creer_employe(self):

        try :
            new_employe = (self.nom, self.prenom, self.salaire, self.id_service)
            connection = mysql.connector.connect(
                host = "localhost",
                user = username,
                password = userpass,
                database = "job07"
            )

            usercurs = connection.cursor()
            
            usercurs.execute("INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)", new_employe)
            connection.commit()
            usercurs.close()
            connection.close()

        except mysql.connector.Error as error:
            print(f"Something went wrong: {error}")

    def supprimer_employe(self):

        try :
            connection = mysql.connector.connect(
                host = "localhost",
                user = username,
                password = userpass,
                database = "job07"
            )

            usercurs = connection.cursor()
        
            usercurs.execute(
                "DELETE FROM employe WHERE id_employe = %s", (self.id_employe)
            )
            connection.commit()
            usercurs.close()
            connection.close()

        except mysql.connector.Error as error:
            print(f"Something went wrong: {error}")


    def afficher_employes(self):
        try :

            connection = mysql.connector.connect(
                host = "localhost",
                user = username,
                password = userpass,
                database = "job07"
            )

            usercurs = connection.cursor()
            
            usercurs.execute(
                """
                SELECT employe.nom, employe.prenom, service.nom
                FROM employe
                JOIN service
                ON employe.id_service = service.id_service
                """
            )
            rows = usercurs.fetchall()
            for r in rows :
                print(r)
            usercurs.close()
            connection.close()

        except mysql.connector.Error as error:
            print(f"Something went wrong: {error}")

    def find_if_rich(self):
        try :

            connection = mysql.connector.connect(
                host = "localhost",
                user = username,
                password = userpass,
                database = "job07"
            )

            usercurs = connection.cursor()
            
            usercurs.execute("SELECT * FROM employe WHERE salaire > 3000;")
            rows = usercurs.fetchall()
            for r in rows :
                print(r)
            usercurs.close()
            connection.close()

        except mysql.connector.Error as error:
            print(f"Something went wrong: {error}")

