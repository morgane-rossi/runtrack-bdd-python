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
    usercurs.execute("SELECT nom, capacite FROM salle;")
    rows = usercurs.fetchall()
    print(rows)
    usercurs.close()
    connection.close()

except mysql.connector.Error as error:
    print(f"Something went wrong: {error}")
