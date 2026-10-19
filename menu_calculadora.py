print("="*20)
print("MENU DE OPÇÕES")
print("="*20)
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
opcao = int(input("Escolha uma opção: "))
if opcao == 1:
    print(f"O resultado da sua soma é {numero1+numero2}")
elif opcao == 2:
    print(f"O resultado da sua subtração é {numero1-numero2}")
elif opcao == 3:
    print(f"O resultado da sua multiplicação é {numero1*numero2}")
elif opcao == 4:
    if numero2 == 0:
        print("Não é possivel dividir por 0.") 
    else:
        print(f"O resultado da sua divisão é {numero1/numero2}")
else:
    print("Opção inválida")