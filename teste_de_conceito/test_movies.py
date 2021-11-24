from typing import Dict
import requests
import json
from ast import literal_eval


# URL principal de acesso ao servidor       
url_base = 'http://127.0.0.1:8000/movies/'

def cad_filme():
    """
    cadastra filme
    """

    print('\n==>Cadastrar filme:')
    xtitle       = input("        Título: ")
    xdirector    = input("       Diretor: ")
    xyear        = int(input("Ano Lançamento: "))
    xdescription = input("     Descrição: ")

    d = {'title': xtitle, 
         "director": xdirector,
         "description": xdescription,
         "release_year": xyear}
    print(d)
    print(f'Requisição post: {url_base}')
    print(f'data: {data}')
    r = requests.post(url_base, data=d)
    if r.status_code == 201:
        print("Filme cadastrado com sucesso!\n")
    else:
        print(f"Erro: {r.status_code}")


def consult_filme():
    """
    Consulta filme
    """

    print('==>Consulta filme:')
    id_movie = input("Entre com o ID do filme: ")
    url = f'{url_base}{id_movie}'
    print(f'Requisição get: {url}')
    r = requests.get(url)
    if (r.status_code >= 400 and r.status_code <= 499):
        print("Filme não localizado!")
    else:
        print("Filme consultado:")
        response = r.text
        filme    = literal_eval(response)
        print(filme)
        

def list_filmes():
    """
    Lista filmes
    """

    print('==>Listar filmes:')
    print(f'Requisição get: {url_base}')
    r = requests.get(url_base)
    response = r.text
    list_dict = literal_eval(response)
    for dict in list_dict:
        print(dict)


def exc_filme():
    """
    Exclusão filme
    """
    
    print('==>Exclusão de filme:')
    id_movie = input("Entre com o ID do filme: ")
    url = f'{url_base}{id_movie}'
    print(f'Requisição delete: {url}')
    r = requests.delete(url)
    
    if (r.status_code >= 200 and r.status_code <= 299):
        print(f"Filme excluído com sucesso: {r}")
    else:
        print(f"Filme não localizado!: {r}")


def alt_filme():
    """
    Consulta filme
    """
    print('==>Altera dados do:')
    id_movie = input("Entre com o ID do filme: ")
    url = f'{url_base}{id_movie}'
    print(f'Requisição get: {url}')
    r = requests.get(url)
    if (r.status_code >= 400 and r.status_code <= 499):
        print("Filme não localizado!")
    else:
        print("Filme consultado:")
        response = r.text
        filme    = literal_eval(response)

        print("    Título: ", filme["title"])
        print("   Diretor: ", filme["director"])
        print("Lançamento: ", filme["release_year"])
        print(" Descrição: ", filme["description"])
        print("\n==>Entre com os novos dados!")

        xtitle       = input("        Título: ")
        xdirector    = input("       Diretor: ")
        xyear        = int(input("Ano Lançamento: "))
        xdescription = input("     Descrição: ")

        d = {"id_movies": id_movie,
             'title': xtitle, 
             "director": xdirector,
             "description": xdescription,
             "release_year": xyear,
             'create_at': filme['create_at']}
        
        
        url  = f'{url_base}{id_movie}/'
        print(f'Requisição patch: {url}')
        print(f'data: {data}')
        r = requests.patch(url, data=d, )
        
        if r.status_code == 200:
            print("==>>Filme alterado com sucesso!\n")
        else:
            print(f"\n==>>Alteração NÃO realizada. <<< Erro: {r.status_code}>>>\n")


def main():

    flag = 1
    while flag != 0:
        print("\n")
        print("=========M E N U=========")
        print("1 - Cadastrar Filme")
        print("2 - Consultar Filme")
        print("3 - Listar Filmes")
        print("4 - Excluir Filme")
        print("5 - Alterar Dados")
        print("0 - Sair")
        print("=========================")
        op = input("Entre com o número da opção: ")
        print("\n")
        if op == "1":
            cad_filme()
        elif op == "2":
            consult_filme()
        elif op == "3":
            list_filmes()
        elif op == "4":
            exc_filme()
        elif op == "5":
            alt_filme()
        else:
            break


#Chama Função Principal
if __name__ == '__main__':
    main()
