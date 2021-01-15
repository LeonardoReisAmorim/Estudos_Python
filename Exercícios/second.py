""" 
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um script que leia o nome dos quatro alunos e mostre a ordem sorteada
"""
from random import choices #importei a biblioteca random com a função que faz uma ordem aleatoria

i = 1 #inicializei o contador do loop
alunos = [] #inicializei o vetor

# fazendo um loop para ler o nome dos alunos
while i <= 4: 
    alunos.append(input("digite o nome do aluno"))
    i+=1

# mostrei os nomes dos alunos
print(choices(alunos, k=len(alunos)))
#o primeiro parametro é o array, e o segundo é até qtd de casas(array) que vai ser ordenado, no caso como tem quatro alunos, irá na ordem de apresentação aleatoria