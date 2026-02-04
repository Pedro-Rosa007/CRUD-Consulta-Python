# CRUD de Consultas 

Sistema de gerenciamento de consultas desenvolvido em Python utilizando interface gráfica moderna com `CustomTkinter` e persistência de dados em `MySQL`.

## 🚀 Funcionalidades
* **Cadastro**: Registro de pacientes e detalhes da consulta.
* **Leitura**: Visualização em tempo real via Treeview (Tabela).
* **Atualização**: Edição de dados ao clicar duas vezes no registro.
* **Exclusão**: Remoção de registros do banco de dados.

## 🛠️ Tecnologias Utilizadas
* [Python 3.x](https://www.python.org/)
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (Interface UI)
* [MySQL](https://www.mysql.com/) (Banco de Dados)
* [tkcalendar](https://pypi.org/project/tkcalendar/) (Seleção de datas)

## 📋 Pré-requisitos & Instalação

Como este projeto utiliza um **servidor MySQL local**, siga os passos abaixo:

### 1. Configurar o Banco de Dados
1. Certifique-se de ter o XAMPP, WAMP ou MySQL Server instalado.
2. Crie um banco de dados chamado `bdcrud`.
3. Execute o script contido no arquivo `setup_db.sql` para criar a tabela necessária.

### 2. Configurar Conexão
Se o seu MySQL tiver uma senha ou porta diferente de 3306, altere as configurações no método database() dentro do arquivo crudv2.py:

Python
self.conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'SUA_SENHA_AQUI',
    database = 'bdcrud'
)

