#Vetores:
num: int
num = int(input("Quantos números você quer digitar no vetor? "))

vetor: [float] = [0 for x in range(num)]

for i in range(0, num):
    vetor[i] = float(input("Digite um número: "))

print()
print("Números Digitados:")

for i in range(0, num):
    print(f"{vetor[i]:.1f}")

#Matrizes:
numLin: int = int(input("Digite quantas linhas vai ter a matriz: "))
numCol: int = int(input("Digite quantas colunas vai ter a matriz: "))

matriz: [[int]] = [[0 for x in range(numCol)] for x in range(numLin)]

for i in range(0, numLin):
    for j in range(0, numCol):
        matriz[i][j] = int(input(f"Elemento [{i},{j}]: "))

print()
print("Matriz Digitada:")

for i in range(0, numLin):
    for j in range(0, numCol):
        print(f"{matriz[i][j]} ", end="")
    print()

