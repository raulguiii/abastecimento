banco: 

CREATE DATABASE db_abastecimento_semecti; 
USE db_abastecimento_semecti;

-- Tabela Usuários
-- Para criar usuario o departamento deve ser informado dessa forma 'Admin','Almoxarifado','Comunicação', 'DEE', 'Casa_de_Projetos', 'Engenharia_Manutenção', 'Engenharia_Projetos', 'Gabinete','Logística', 'Informática', 'Núcleo', 'Nutrição', 'Supervisão', 'Vigilância'
-- Qualquer departamento escrito diferente vai dar pau
Select * from usuarios;
CREATE TABLE usuarios ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
	nome_completo VARCHAR(255) NOT NULL, 
	senha VARCHAR(255) NOT NULL, 
	cargo VARCHAR(100) NOT NULL, 
	departamento VARCHAR(100) NOT NULL, 
	rgf VARCHAR(50) UNIQUE NOT NULL 
);
INSERT INTO usuarios (nome_completo, senha, cargo, departamento, rgf) VALUES ('Joel', 'Joel10', 'Chefe de Departamento', 'Engenharia_Manutenção', '85410');

UPDATE usuarios 
SET 
    nome_completo = 'Jessica Freitas', 
    senha = 'JessicaFreitas10', 
    cargo = 'Chefe de Departamento', 
    departamento = 'Gabinete', 
    rgf = '87410' 
WHERE id = 3;


-- Tabela Almoxarifado
Select * from abastecimentoAlmox;
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


-- Tabela Casa de Projetos
Select * from abastecimentoCasaDeProjetos;
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


-- Tabela Comunicação
Select * from abastecimentoComunicacao;
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


-- Tabela DEE
Select * from abastecimentoDEE;
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


-- Tabela Engenharia Manutenção
Select * from abastecimentoEng1;
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


-- Tabela Engenharia Projetos
Select * from abastecimentoEng2;
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


-- Tabela Gabinete
Select * from abastecimentoGabinete;
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


-- Tabela Informática
Select * from abastecimentoInformatica;
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


-- Tabela Logística
Select * from abastecimentoLogistica;
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


-- Tabela Núcleo
Select * from abastecimentoNucleo;
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


-- Tabela Nutrição 
Select * from abastecimentoNutricao;
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


-- Tabela Supervisao 
Select * from abastecimentoSupervisao;
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


-- Tabela Vigilancia 
Select * from abastecimentoVigilancia;
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




