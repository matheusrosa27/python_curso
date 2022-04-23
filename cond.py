hora: int

hora = int(input("Digite a hora atual: "))

#Uso do IF, ELSE IF e ELSE
if hora<=12:
    print(f"Bom dia!")
elif hora<=18:
    print(f"Boa tarde!")
elif hora<=23:
    print(f"Boa noite!")
else:
    print(f"Hora errada! Tem certeza que está na Terra?")

x: int
soma: int
y: int

x = int(input(f"Digite um número: "))
soma = 0
y = 0

#Uso do WHILE
while x != 0:
    soma = soma + x
    y = y+1
    x = int(input(f"Digite outro número: "))

print(f"Você digitou {y} números e obteve um total de: {soma}")