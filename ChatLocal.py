from serverTCP import sala
from clientTCP import cliente

print("O que você deseja fazer?")
print("1 - Criar novo chat")
print("2 - Entrar em uma sala já existente")
escolha = input(": ")
if escolha=="1":
    sala()
elif escolha=="2":
    cliente()
else:
    print("Essa opção é invalida")