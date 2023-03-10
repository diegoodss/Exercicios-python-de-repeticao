'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
eles.'''

num1=int(input('Digite um numero inteiro: '))
num2=int(input('Digite um numero inteiro: '))
if num1<num2:
    for i in range (num1+1,num2,1):
        print('O numero entre {} e {} é {}'.format(num1, num2, i))

else:
    a=num2
    b=num1
    for i in range (a+1,b,1):
        print('O numero entre {} e {} é {}'.format(num1,num2,i))
