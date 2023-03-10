'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre
1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser
conforme o exemplo abaixo:'''

num=int(input('Escolja um numero da tabuada: '))
print('A tabuada de {} é : '.format(num))
t = ''
l = t.center(15, '*')
print(l)
for i in range(1,11):
    tab=num*i
    print('{} x {} = {}'.format(num,i,tab))
t = ''
l = t.center(15, '*')
print(l)