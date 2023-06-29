# Spotter

A ferramenta desenvolvida tem como objetivo permitir ao usuário gerar uma base a partir de comentários disponíveis nas redes sociais através de suas APIs e armazená-las em um banco de dados, sendo possível filtrar os comentários por palavras-chaves ou tópicos.

A interface da ferramenta foi desenvolvida utilizando a biblioteca _Qt_ para Python, _PyQt_. O _backend_ foi desenvolvido utilizando Python, além de fazer usos de bibliotecas para comunicação com o banco de dados não estruturado MongoDB, _PyMongo_.

Para mais informações acesse a documentação do projeto no PDF **Documentacao** localizado na raíz do projeto clonado ou no repositório.

## Instalação

Para utilizar a aplicação, o usuário deverá instalar algumas dependências. É necessário ter instalado o Python $\geq$ 3.10, disponibilizado para download na página oficial do [Python](https://www.python.org/downloads/), o [Git](https://git-scm.com/downloads) que será utilizado para baixar o código fonte da aplicação e por fim o MongoDB, seguindo o [manual de instalação](ttps://www.mongodb.com/docs/manual/installation/) disponível no site do sistema.

Após isso, clone o repositório do projeto.

```
$ git clone https://github.com/venigarcia/spotter_pfp.git
```

Para instalar as dependências de bibliotecas do Python execute o comando abaixo na raíz do projeto.

```
$ pip install -r requirements.txt
```

## Executando a aplicação
Para iniciar a aplicação após a instalação das dependências deverá executar o comando:

```
$ python app.py
```

## Testes de unidade

Após o processo de instalação, abra um terminal de comando na raíz do projeto e execute o comandao abaixo:

```
$ python -W ignore -m unittest tests.<NomeDoModuloDeTeste>.<NomeDoTeste> -v
```

Substitua os valores entre "$< >$" pelo nome do módulo de teste e pelo nome do teste. Essas informações podem ser encontradas na documentação da aplicação na raíz do projeto clonado ou no repositório.

Para os testes do módulo de teste _TestRedditAPI_ será necessário informar as chaves de acesso a API através de variáveis de ambiente, são elas _API\_USER_, nome de usuário; _API\_PASSWORD_, senha de usuário; _API\_KEY_, key fornecida pela plataforma e _API\_SECRET\_KEY_, secret key fornecida pela plataforma.

Para definir uma variável de ambiente no Windows use o comando:

```
$ set <NomeDaVariável>=<ValorDaVariável>
```