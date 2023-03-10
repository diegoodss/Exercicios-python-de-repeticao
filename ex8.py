'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

for i in range (0,5):
    numero=int(input('Digite um numero: '))
soma=numero*5
media=soma/5
print('Soma: {}\nMedia: {:.2f} '.format(soma,media))