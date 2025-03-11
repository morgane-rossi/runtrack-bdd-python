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
    usercurs.execute("SELECT * FROM etudiant;")
    rows = usercurs.fetchall()
    for r in rows :
        print(r)

    usercurs.close()
    connection.close()

except mysql.connector.Error as error:
    print(f"Something went wrong: {error}")
