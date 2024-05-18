def soma(x,y):
  return x + y

def subtracao(x,y):
  return x - y

def multiplicacao(x,y):
  return x * y

def divisao(x,y):
  return x / y

print("Selecione uma operação")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Escolha uma opção (1,2,3,4)")

if escolha in ('1','2','3','4'):
  n1 = float(input("Digite um número: "))
  n2 = float(input("Digite outro número: "))

  if escolha == '1':
    print(soma(n1,n2))

  if escolha == '2':
    print(subtracao(n1,n2))

  if escolha == '3':
    print(multiplicacao(n1,n2))

  if escolha == '4':
    print(divisao(n1,n2))