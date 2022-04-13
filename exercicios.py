# Exercício 1
print ("Digite um número de 0 a 3")
num = int(input())
if (num == 0):
    print ("zero")
if (num == 1):
    print ("um")
if (num == 2):
    print ("dois")
if (num == 3):
    print ("três")

# Exercício 2
print ("Digite a Temperatura")
temp = float(input())
if (temp > 30):
    print ("Perigo, Superaquecimento")

# Exercício 3
print ("Digite a Temperatura")
temp = float(input())
if (temp > 30):
    print ("Perigo, Superaquecimento")
else:
    print ("Temperatura Normal")

# Exercício 4
print ("Digite o nome do cliente")
cli = str(input())
print ("Digite o valor da compra")
buy = float(input())
print ("Digite a condição de pagamento")
print ()
print ("(1)Á Vista")
print ("(2)Parcelado")
pag = int(input())
if (pag == 1):
    val = buy-(buy*0.07)
    print ("Nome do Cliente: ",cli)
    print ("Forma de Pagamento: Á Vista")
    print ("Valor do Produto: R$",buy)
    print ("Valor com desconto: R$",val)
else:
    print ("Nome do Cliente: ",cli)
    print ("Forma de Pagamento: Parcelado")
    print ("Valor do Produto: R$",buy)

# Exercício 5
print ("Digite um número de 0 a 3")
num = int(input())
if (num == 0):
    print ("zero")
elif (num == 1):
    print ("um")
elif (num == 2):
    print ("dois")
elif (num == 3):
    print ("três")
else:
    print ("Digite o número pedido")

# Exercício 6
print ("Digite 3 números")
n1 = int(input())
n2 = int(input())
n3 = int(input())
if (n1 > n2 and n1 > n3):
    print ("maior:",n1)
elif (n2 > n1 and n2 > n3):
    print ("Maior:",n2)
elif (n3 > n2 and n3 > n1):
    print ("Maior:",n3)
