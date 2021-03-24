import requests
from bs4 import BeautifulSoup as bs

usuario_github = input("Digite o nome do usuário para retornar a foto ")
url = "https://www.github.com/" +usuario_github #retorna o link da página do usuário
r = requests.get(url) #guarda o request em r
pagina = bs(r.content, "html.parser") #content pega todo html da pagina
perfil = pagina.find("img", {"alt" : "Avatar"})["src"]
print(perfil)