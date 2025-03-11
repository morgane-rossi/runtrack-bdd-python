import mysql.connector
import data
username = data.personnel[0]
userpass = data.personnel[1]

try :
    connection = mysql.connector.connect(
        host = "localhost",
        user = username,
        password = userpass,
        database = "LaPlateforme"
    )

    usercurs = connection.cursor()
    # capacité totale des salles
    usercurs.execute("SELECT capacite FROM salle;")
    rows = usercurs.fetchall()
    total = 0
    for r in rows :
        total += r[0]
    print(f"La capacite de toutes les salles est de : {total}")

    usercurs.close()
    connection.close()

except mysql.connector.Error as error:
    print(f"Something went wrong: {error}")
