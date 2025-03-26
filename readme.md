banco: 

CREATE DATABASE db_abastecimento_semecti; 

USE db_abastecimento;

CREATE TABLE usuarios ( id INT AUTO_INCREMENT PRIMARY KEY, nome_completo VARCHAR(255) NOT NULL, senha VARCHAR(255) NOT NULL, cargo VARCHAR(100) NOT NULL, departamento VARCHAR(100) NOT NULL, rgf VARCHAR(50) UNIQUE NOT NULL );

select * from usuarios;

INSERT INTO usuarios (nome_completo, senha, cargo, departamento, rgf) VALUES ('Raul', 'teste', 'Chefe', 'TI', '123456');

INSERT INTO usuarios (nome_completo, senha, cargo, departamento, rgf) VALUES ('Raul', 'teste', 'Chefe', 'TI', '2005');

CREATE TABLE abastecimentoAlmox ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    rgf VARCHAR(50) NOT NULL, 
    km INT NOT NULL, 
    placa VARCHAR(20) NOT NULL, 
    data DATE NOT NULL, 
    posto VARCHAR(255) NOT NULL, 
    comprovante VARCHAR(255) NOT NULL, 
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
    comprovante VARCHAR(255) NOT NULL,
    FOREIGN KEY (rgf) REFERENCES usuarios(rgf) 
);

select * from abastecimentoCasaDeProjetos;


CREATE TABLE abastecimentoComunicacao ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    rgf VARCHAR(50) NOT NULL, 
    km INT NOT NULL, 
    placa VARCHAR(20) NOT NULL, 
    data DATE NOT NULL, 
    posto VARCHAR(255) NOT NULL, 
    comprovante VARCHAR(255) NOT NULL,
    FOREIGN KEY (rgf) REFERENCES usuarios(rgf) 
);


select * from abastecimentoComunicacao;



CREATE TABLE abastecimentoDEE ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    rgf VARCHAR(50) NOT NULL, 
    km INT NOT NULL, 
    placa VARCHAR(20) NOT NULL, 
    data DATE NOT NULL, 
    posto VARCHAR(255) NOT NULL, 
    comprovante VARCHAR(255) NOT NULL,
    FOREIGN KEY (rgf) REFERENCES usuarios(rgf) 
);


select * from abastecimentoDEE;


CREATE TABLE abastecimentoEng1 ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    rgf VARCHAR(50) NOT NULL, 
    km INT NOT NULL, 
    placa VARCHAR(20) NOT NULL, 
    data DATE NOT NULL, 
    posto VARCHAR(255) NOT NULL, 
    comprovante VARCHAR(255) NOT NULL,
    FOREIGN KEY (rgf) REFERENCES usuarios(rgf) 
);


select * from abastecimentoEng1;


CREATE TABLE abastecimentoEng2 ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    rgf VARCHAR(50) NOT NULL, 
    km INT NOT NULL, 
    placa VARCHAR(20) NOT NULL, 
    data DATE NOT NULL, 
    posto VARCHAR(255) NOT NULL, 
    comprovante VARCHAR(255) NOT NULL,
    FOREIGN KEY (rgf) REFERENCES usuarios(rgf) 
);

select * from abastecimentoEng2;


CREATE TABLE abastecimentoGabinete ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    rgf VARCHAR(50) NOT NULL, 
    km INT NOT NULL, 
    placa VARCHAR(20) NOT NULL, 
    data DATE NOT NULL, 
    posto VARCHAR(255) NOT NULL, 
    comprovante VARCHAR(255) NOT NULL,
    FOREIGN KEY (rgf) REFERENCES usuarios(rgf) 
);

select * from abastecimentoGabinete;


CREATE TABLE abastecimentoInformatica ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    rgf VARCHAR(50) NOT NULL, 
    km INT NOT NULL, 
    placa VARCHAR(20) NOT NULL, 
    data DATE NOT NULL, 
    posto VARCHAR(255) NOT NULL, 
    comprovante VARCHAR(255) NOT NULL,
    FOREIGN KEY (rgf) REFERENCES usuarios(rgf) 
);

select * from abastecimentoInformatica;


CREATE TABLE abastecimentoLogistica ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    rgf VARCHAR(50) NOT NULL, 
    km INT NOT NULL, 
    placa VARCHAR(20) NOT NULL, 
    data DATE NOT NULL, 
    posto VARCHAR(255) NOT NULL, 
    comprovante VARCHAR(255) NOT NULL,
    FOREIGN KEY (rgf) REFERENCES usuarios(rgf) 
);

select * from abastecimentoLogistica;


CREATE TABLE abastecimentoNucleo ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    rgf VARCHAR(50) NOT NULL, 
    km INT NOT NULL, 
    placa VARCHAR(20) NOT NULL, 
    data DATE NOT NULL, 
    posto VARCHAR(255) NOT NULL, 
    comprovante VARCHAR(255) NOT NULL,
    FOREIGN KEY (rgf) REFERENCES usuarios(rgf) 
);

select * from abastecimentoNucleo;



CREATE TABLE abastecimentoNutricao ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    rgf VARCHAR(50) NOT NULL, 
    km INT NOT NULL, 
    placa VARCHAR(20) NOT NULL, 
    data DATE NOT NULL, 
    posto VARCHAR(255) NOT NULL, 
    comprovante VARCHAR(255) NOT NULL,
    FOREIGN KEY (rgf) REFERENCES usuarios(rgf) 
);

select * from abastecimentoNutricao;



CREATE TABLE abastecimentoSupervisao ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    rgf VARCHAR(50) NOT NULL, 
    km INT NOT NULL, 
    placa VARCHAR(20) NOT NULL, 
    data DATE NOT NULL, 
    posto VARCHAR(255) NOT NULL, 
    comprovante VARCHAR(255) NOT NULL,
    FOREIGN KEY (rgf) REFERENCES usuarios(rgf) 
);

select * from abastecimentoSupervisao;


CREATE TABLE abastecimentoVigilancia ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL, 
    rgf VARCHAR(50) NOT NULL, 
    km INT NOT NULL, 
    placa VARCHAR(20) NOT NULL, 
    data DATE NOT NULL, 
    posto VARCHAR(255) NOT NULL, 
    comprovante VARCHAR(255) NOT NULL,
    FOREIGN KEY (rgf) REFERENCES usuarios(rgf) 
);

select * from abastecimentoVigilancia;