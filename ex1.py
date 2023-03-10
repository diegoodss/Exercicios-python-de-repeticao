'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido.'''

nota=int(input('Digite um numero de 0 a 10: '))
while nota > 10 or nota < 0:
    nota=int(input('Digite um numero Valido de 0 a 10: '))
print(nota)