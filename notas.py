notas = []
while True:
    nota = float(input("Digite a nota do aluno (ou -1 para sair): "))
    
    if nota == -1: # quando digitado -1 ele ira parar
        break
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"Média do aluno: {media:.2f}")

if media >= 6:
    print("Aluno Aprovado!") # nota maior que 6 esta aprovado
elif 5 <= media < 6:
    print("Aluno em Recuperação!") # se for menor que 6 esta de rucuperação
else:
    print("Aluno Reprovado!")