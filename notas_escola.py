nota = int(input("Digite a nota final do aluno 1 á 10 (Número inteiro): "))
if nota < 0 or nota > 10:
    print("Nota inválida!!")
elif nota == 10:
    print("Excelente!!")
elif nota >= 7:
    print("Boa nota.")
elif nota >= 5:
    print("Regular")
else:
    print("Nota insuficiente para ser aprovado.")
 