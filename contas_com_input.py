print("="*10, "QUESTÃO 1", "="*10)
produto = input("Qual produto comprado? ")
preco_produto = float(input("Qual o preço do produto? "))
quantidade = int(input("Qual a quantidade comprada? "))
total_gasto = preco_produto*quantidade
print("O total gasto foi:", "R$:",total_gasto)

print("="*10, "QUESTÃO 2", "="*10)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2
print("A média do aluno foi:", media)

print("="*10, "QUESTÃO 3", "="*10)
reais = float(input("Digite o valor em reais que deseja gastar: "))
dolar = (5.04)
conversao = reais//dolar
print(f"A quantidade de dolar que consegue comprar é",conversao, "dolares")

print("="*10, "QUESTÃO 4", "="*10)
salario = float(input("Digite seu salário: "))
aumento = (0.10)
salarioaumento = salario*aumento
salarioatual = salario + salarioaumento
print("Seu salário com o aumento de 10% é:", salarioatual)