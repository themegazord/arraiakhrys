# API - Banco de dados ArraiaKhrys | :hammer_and_wrench: In Building

# Objetivo

Esse readme tem como objetivo principal auxiliar os desenvolvedores mobile e front-end a como consumirem a API tanto local, quanto em produção.

## Instalação do MySQL Workbench

Para utilizar da API local e ter acesso ao banco de dados, você irá ter que instalar o MySQL Workbench, ou outro manipulador de banco de dados MySQL. Você pode baixar o MySQL Workbench clicando **[aqui](https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.29.0.msi)**

Caso precise de um tutorial de como configurar, clique **[aqui](https://www.youtube.com/watch?v=zpssr3u1EO8)** 
> Todos os direitos aos criadores do vídeo.


**Observação:**

*Ao configurar o MySQL Workbench, configure-o como:*

1. Usuário: megad3v
2. Senha: superonze02!
3. Nome do banco de dados: arraiakhrys
4. Porta: 3306
5. Host: 127.0.0.1


## Instalações do Back-end

Após você ter ou clonado, ou dado _fork_ no repositório extraído em sua máquina, você irá abrir seu terminal dentro da pasta e dar os seguintes comandos:

- Para criar o ambiente virtual no seu arquivo:
```
python -m venv venv
```
- Para habilitar o ambiente virtual:
```
venv\Scripts\activate
```
- Para instalar todos os componentes do requirements.txt
```
pip install -r requirements.txt
```
- Para rodas todas as migrações pendentes para o banco de dados.
```
python manage.py migrate
```

## Usuabilidade

Para ligar o servidor:

```
python manage.py runserver
```

Com o servidor ligado, basta consumir suas api's.


Cadastro - arraiakhrys/signup/api/