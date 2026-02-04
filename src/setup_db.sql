CREATE DATABASE IF NOT EXISTS bdcrud;
USE bdcrud;

CREATE TABLE IF NOT EXISTS dados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    telefone VARCHAR(50),
    data DATE,
    estado VARCHAR(100),
    sobre TEXT
);