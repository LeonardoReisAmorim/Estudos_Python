""" 
Um professor quer sortear um dos seus 4(quatro) alunos para apagar o quadro. faça um script que leia
o nome dos alunos e escreva o nome do aluno escolhido
"""
from random import randint #importei a biblioteca random com a função que sorteia um numero inteiro

i = 1 #inicializei o contador do loop
alunos = [] #inicializei o vetor

# fazendo um loop para ler o nome dos alunos
while i <= 4: 
    alunos.append(input("digite o nome do aluno"))
    i+=1

#sorteia o aluno
sorteado = randint(0, len(alunos))

# mostra o nome do aluno sorteado
print(alunos[sorteado])



