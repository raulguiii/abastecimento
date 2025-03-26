banco: 

CREATE DATABASE db_abastecimento;
USE db_abastecimento;


CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    departamento VARCHAR(100) NOT NULL,
    rgf VARCHAR(50) UNIQUE NOT NULL
);

select * from usuarios;

INSERT INTO usuarios (nome_completo, senha, cargo, departamento, rgf)
VALUES ('Raul', 'teste', 'Chefe', 'TI', '123456');


CREATE TABLE abastecimentoAlmox (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    rgf VARCHAR(50) NOT NULL,
    km INT NOT NULL,
    placa VARCHAR(20) NOT NULL,
    data DATE NOT NULL,
    posto VARCHAR(255) NOT NULL,
    comprovante VARCHAR(255) NOT NULL, -- Caminho do arquivo salvo no servidor
    FOREIGN KEY (rgf) REFERENCES usuarios(rgf)
);

select * from abastecimentoAlmox;

CREATE TABLE abastecimentoCasaDeProjetos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    rgf VARCHAR(50) NOT NULL,
    km INT NOT NULL,
    placa VARCHAR(20) NOT NULL,
    data DATE NOT NULL,
    posto VARCHAR(255) NOT NULL,
    comprovante VARCHAR(255) NOT NULL, -- Caminho do arquivo salvo no servidor
    FOREIGN KEY (rgf) REFERENCES usuarios(rgf)
);

select * from abastecimentoCasaDeProjetos;



