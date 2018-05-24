# Analise de Log

Projeto para analisar um Banco de Dados, e responder diversas perguntas usando python3 e psql

# Pré-requisito

* Python 3
* Psycopg2
* PostgreSql
* Vagrant
* VirtualBox

# Como funciona

O projeto roda em um banco de dados fictício, onde existem postagem, usuários e etc.
Utilizando Python3, fazemos uma serie de consultas no DB, para assim responder as perguntas e mostrar o resultado no terminal

# Executando o código

Primeiro clone o repositório:

    $ git@github.com:rafaelvebercarvalho/udacity-logs.git

Instale o VirtualBox e depois o Vagrant.

Com a VM devidamente configurada, com Python3, Psycopg2 e PostgreSql.

Baixe o sql schema:

* https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Com o arquivo newsdata.sql dentro da VM, execute em seu terminal:

    $ psql -d news -f newsdata.sql

Com isso iremos criar 3 tabelas:

* Authors
* Articles
* Log

Com tudo configurado, rode o arquivo logs.py:

    $ python logs.py

# Aviso

Esse projeto foi feito com intuito educacional, qualquer duvida entrar em contato.
