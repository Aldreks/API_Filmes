# Project LIVOX:  Consult Movies

## Objetivo:
  Fazer API Rest em Django, usando a linguagem Python.


## Finalidade do Projeto:
  Armazenar dados sobre filmes num banco de dados, consulta, atualização e deleção de filmes, (CRUD).
  

## Importância:
  Avaliar nível de domínio sobre a linguagem Python e criação e utilização de API (Application Programming Interface) usando Django. 


## Como instalar e ativar o ambiente virtual em Django:

- Entre no prompt de comando (CMD) do windows, na pasta em que vai ser criado o programa, e siga as instruções abaixo:

- Criando ambiente virtual:

`python -m venv venv`

- Ativando o ambiente virtual VENV. Entre neste caminho e rode o Activate: 

`venv\Scripts\activate`

- Instalação local das dependências Django:  

`pip install django djangorestframework`

- Ativando o servidor local criado em Django (Digitar dentro da pasta do projeto criado):  

`python manage.py runserver`

- caso apresente erro na ativação local do servidor, por falta de tabelas no banco de dados, digitar:  

`python manage.py migrate`


## Ativando o projeto:

- `venv\Scripts\activate`
- `python manage.py runserver`
- `http://127.0.0.1:8000/movies`

- Ao findar o uso do app, desativar o ambiente virtual estando dentro da pasta do mesmo, digitando: 'deactivate'


## Como funciona o aplicativo?

- No prompt do Windows (usando CMD), na pasta do projeto, subpasta `teste_de_conceito` executar  o comando 
  `python test_movies.py` e será exibido um menu interativo com as opções de processamento. Lá é possível testar 
  todo o CRUD do projeto.
  
- outra forma de operacionalizar o projeto é aplicando a url (IP) indicada ao rodar `python manage.py runserver` + `movies`, no browser.
  
  ex.:  `http://127.0.0.1:8000/movies`

- Você pode usar também um programa como `Insomnia` para testar os métodos via http no link do seu servidor local. Lá você pode testar o CRUD.


## Desenvolvedor:

- Aldreks Albuquerque 
[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/Aldreks)](https://github.com/Aldreks)
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=//linkedin.com/in/aldreks-albuquerque-92b46797)](//linkedin.com/in/aldreks-albuquerque-92b46797)

[Google](https://www.google.com/)


## Gerente do Projeto:

|        NOME       |          ÁREA           |
|-------------------|-------------------------|
|  Vinícius Souza   |  desenvolvimento Livox  |


## Linguagem de Desenvolvimento Utilizada e Aplicativos:

  Este projeto foi desenvolvido em Python. Apps utilizados: 
  
  <table>
  <tr>
    <td>Python</td>
    <td>Django</td>    
    <td>API Rest</td>
    <td>VS Code</td>
  </tr>
  <tr>
    <td>3.9.7</td> 
    <td>3.2.9</td>
    <td> -- </td>
    <td>1.62.3</td>
  </tr>
</table>


## Outras Bibliotecas utilizadas:

`ast, json, requests, typing`



