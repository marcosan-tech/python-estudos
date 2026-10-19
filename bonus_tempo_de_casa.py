print("="*20)
print("CÁLCULO DE BONUS POR TEMPO DE CASA")
print("="*20)
salario = float(input("Digite seu salário atual: "))
tempodecasa = int(input("Há Quantos anos você trabalha na empresa? "))
bonusdezmais = salario*0.20
bonuscincomais = salario*0.10
if tempodecasa < 0:
     print("Tempo de casa inválido.")
elif tempodecasa >= 10:
    salariofinal =  salario + bonusdezmais
    print(f"Você recebeu um bonus de R${bonusdezmais:.2f} pelo seu tempo de casa.")
    print(f"Seu salário passa a ser R${salariofinal:.2f}")
elif tempodecasa >= 5:
        salariofinal =  salario + bonuscincomais
        print(f"Você recebeu um bonus de R${bonuscincomais:.2f} pelo seu tempo de casa.")
        print(f"Seu salário passa a ser R${salariofinal:.2f}")
else: 
    print("Você não tem direito a bonus no momento.")
