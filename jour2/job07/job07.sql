
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

INSERT INTO service (nom) VALUES ("comptabilite");
INSERT INTO service (nom) VALUES ("developpement logiciel");
INSERT INTO service (nom) VALUES ("cybersecurite");
INSERT INTO service (nom) VALUES ("intelligence artificielle");
INSERT INTO service (nom) VALUES ("club musique");

/*
Requête pour récupérer  tous les employés
dont le salaire est supérieur à 3000€
*/
SELECT *
FROM employe
WHERE salaire > 3000;