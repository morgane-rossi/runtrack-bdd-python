CREATE TABLE type_cage(
    id_type INT NOT NULL AUTO_INCREMENT,
    description VARCHAR(255) NOT NULL,
    PRIMARY KEY(id_type)
);

CREATE TABLE cage(
    id_cage INT NOT NULL AUTO_INCREMENT,
    superficie INT,
    capacite_max INT,
    PRIMARY KEY(id_cage),
    CONSTRAINT FK_type_cage_cage FOREIGN KEY()
);

CREATE TABLE animal(
    id_animal INT NOT NULL AUTO_INCREMENT,
    nom VARCHAR (255) NOT NULL,
    race VARCHAR (255) NOT NULL,
    id_type INT,
    date_naissance DATE,
    pays VARCHAR(25),
    PRIMARY KEY(id_animal),
    CONSTRAINT FK_type_cage_animal FOREIGN KEY(id_type) REFERENCES type_cage(id_type)
);


/*
CREATE TABLE service (
    id_service INT NOT NULL AUTO_INCREMENT,
    nom VARCHAR (255) NOT NULL,
    PRIMARY KEY(id_service)
);

CREATE TABLE employe(
    id_employe INT NOT NULL AUTO_INCREMENT,
    nom VARCHAR (255) NOT NULL,
    prenom VARCHAR (25) NOT NULL,
    salaire FLOAT NOT NULL,
    id_service INT,
    PRIMARY KEY (id_employe),
        CONSTRAINT FK_service_employe FOREIGN KEY(id_service) REFERENCES service(id_service)
);
*/