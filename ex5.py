'''Altere o programa do exercicio 4 permitindo ao usuário informar as populações e as taxas de
crescimento iniciais. Valide a entrada e permita repetir a operação.'''

a=int(input('Digite a população da cidade a: '))
b= int(input('Digite a população da cidade b: '))
ta=float(input('Digite a taxa da cidade a: '))
tb=float(input('Digite a taxa da cidade b: '))
cont= 0
while a < b:
   a = a + (a*ta/100)
   b = b + (b *tb/100)
   cont=cont+1
print(cont)