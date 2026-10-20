nome = input("Digite seu nome: ")
# usei float invés de int por conta que dificilmente algo que envolva compra da um valor inteiro
valorcompra = float(input("Digite o valor gasto: "))
# valor minimo para obter desconto se nao for cliente vip 
valor_minimo = 500
desconto_avista = valorcompra*0.10  
desconto_cliente_vip = valorcompra*0.05
descontoambos = valorcompra*0.15
clientevip = input("Você é Cliente vip (s/n)? ").lower()
print("1 - À vista")
print("2 - Cartão de crédito em 1x")
print("3 - Parcelado (até 6x sem juros)")
forma_de_pagamento = int(input("Digite a forma de pagamento: "))

if (valorcompra <= 0) or (clientevip != "s" and clientevip != "n") or (forma_de_pagamento <=0 or forma_de_pagamento>=4):
    print("Algo deu errado, tente novamente!!")
elif (valorcompra >= valor_minimo) and (clientevip == "s") and (forma_de_pagamento == 1):
    valorfinal = valorcompra-descontoambos
    print("Você teve um desconto de 15% na sua compra.")
    print(f"O valor final da sua compra fica: R${valorfinal:.2f}")
elif (valorcompra >= valor_minimo) and (clientevip == "n") and (forma_de_pagamento == 1):
    valorfinal = valorcompra-desconto_avista
    print("Você teve um desconto de 10% na sua compra.")
    print(f"O valor final da sua compra fica: R${valorfinal:.2f}")
elif clientevip == "s":
    valorfinal = valorcompra-desconto_cliente_vip
    print("Você teve um desconto de 5% na sua compra.")
    print(f"O valor final da sua compra fica: R${valorfinal:.2f}")
else:
    print("Você não obteve desconto nesta compra.")




