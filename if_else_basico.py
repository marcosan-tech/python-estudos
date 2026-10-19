nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
if idade>=18:
    print("Entrada permitida")
else: print("Entrada barrada, menor de idade.")
 
print("="*10, "QUESTÃO 2", "="*10)
nota1 = float(input("Digite a nota da p1(prova um) "))
nota2 = float(input("Digite a nota da p2(prova dois) "))
media = (nota1+nota2) / 2
if media >= 7:
    print("Aluno aprovado, parabéns!!")
else: print("Aluno reprovado.")
 
print("="*10, "QUESTÃO 3", "="*10)
numeroint = int(input("Digite um numero inteiro "))
if numeroint % 2 == 0:
    print("Esse número é par.")
else: print("Esse número é impar.")
 