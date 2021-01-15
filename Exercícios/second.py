""" 
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um script que leia o nome dos quatro alunos e mostre a ordem sorteada
"""
from random import shuffle #importei a biblioteca random com a função de embaralhamento

i = 1 #inicializei o contador do loop
alunos = [] #inicializei o vetor

# fazendo um loop para ler o nome dos alunos
while i <= 4: 
    alunos.append(input("digite o nome do aluno"))
    i+=1

# o metodo shuffle embaralha a lista
shuffle(alunos)
# mostrei os nomes dos alunos
print(alunos)
