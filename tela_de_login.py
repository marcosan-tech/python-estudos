numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
if numero1 > numero2:
    print("O primeiro número é maior que o segundo.")
elif numero1 == numero2:
    print("os números são iguais.")
else:
    print("O segundo número é maior que o primeiro.")
print("="*10, "QUESTÃO 2", "="*10)
idade = int(input("Digite sua idade: "))
if idade <= 12:
    print("Você é uma criança")
else:
    print("Você não é mais criança")
print("="*10, "QUESTÃO 3", "="*10)
 
print("="*10, "TELA DE LOGIN ADM \n", "DIGITE O USUÁRIO PARA TER ACESSO", "="*10)
usuario = input("Digite o Login do Usuário: ")
senha = input("Digite a senha: ")
if usuario == "marcos123" and senha == "python123":
    print("Acesso ao sistema liberado.")
else:
    print("Usuário ou senha inválidos.")
 