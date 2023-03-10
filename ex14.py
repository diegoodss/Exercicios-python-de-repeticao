'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números
pares e a quantidade de números ímpares.'''

pares=0
impares=0
for i in range(0,10):
    num=int(input('Digite um numero: '))
    soma=num*10
    if num %2 == 0:
        pares +=1
    else:
        impares +1
print('Soma dos numeros: {}\nNumeros pares : {}\nNumeros impares: {} '.format(soma,pares,impares))