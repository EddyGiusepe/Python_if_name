# Data Scientist Jr.: Dr. Eddy Giusepe Chirinos Isidro

'''
Este "PythonProjeto1" é do canal de Lira. O link deste vídeo é: https://www.youtube.com/watch?v=150-dpYG1pg&t=417s

O seguinte link é para poder realizar o "git push" de uma maneira forçada, já que no meu código não estava dando certo:

https://www.atlassian.com/br/git/tutorials/syncing/git-push#:~:text=O%20comando%20git%20push%20%C3%A9,com%20membros%20da%20equipe%20remota.
'''

# Aqui importamos o arquivo "pegar_cotacao" a qual contem a função "pegar_cotacao_atual".
from pegar_cotacao import pegar_cotacao_atual  

with open("precos.txt", "r") as arquivo:
    lista_precos = arquivo.read().split("\n")


for linha in lista_precos:
    mercadoria, valor, moeda = linha.split(",")
    cotacao = pegar_cotacao_atual(moeda, "BRL")
    print(f"{mercadoria} tá custando R${float(cotacao)*float(valor):,.2f} hoje")
