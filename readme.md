banco: 

CREATE DATABASE abastecimento_db;
USE abastecimento_db;


CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    departamento VARCHAR(100) NOT NULL,
    rgf VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO usuarios (nome_completo, senha, cargo, departamento, rgf)
VALUES ('Valter Junior', 'teste', 'Chefe', 'TI', '123456');

