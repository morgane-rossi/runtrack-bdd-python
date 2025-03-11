
CREATE TABLE etage (
    id INT AUTO_INCREMENT
        CONSTRAINT PK_etage PRIMARY KEY,
    nom VARCHAR (255) NOT NULL,
    numero INT NOT NULL,
    superficie INT NOT NULL
);

CREATE TABLE salle (
    id INT NOT NULL AUTO_INCREMENT
        CONSTRAINT PK_salle PRIMARY KEY,
    ,
    nom VARCHAR (255) NOT NULL,
    id_etage INT,
    capacite INT NOT NULL,
        CONSTRAINT FK_etage_salle FOREIGN KEY(id_etage) REFERENCES etage (id)
);
