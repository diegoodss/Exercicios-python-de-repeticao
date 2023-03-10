'''Altere o programa anterior para mostrar no final a soma dos números.'''

num1=int(input('Digite um numero inteiro: '))
num2=int(input('Digite um numero inteiro: '))
if num1<num2:
    for i in range (num1+1,num2,1):
        print('O numero entre {} e {} é: {}'.format(num1, num2, i))
        soma = num1 + num2
        print('A soma dos numeros {} e {} é: {}'.format(num1, num2, soma))
else:
    a=num2
    b=num1
    for i in range (a+1,b,1):
        print('O numero entre {} e {} é {}'.format(num1,num2,i))
        soma=a+b
        print('A soma dos numeros {} e {} é: {}'.format(num1,num2,soma))