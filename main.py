name: str
age: int
gender: str
salary: float
height: float

name = "Matheus Fernandes da Rosa"
age = 20
gender = 'M'
salary = 1600.50
height = 1.75

print(f"Nome: {name}")
print(f"Ano: {age}")
print(f"Gênero: {gender}")
print(f"Salário: {salary:.2f}")
print(f"Altura: {height}")

#Uso de placeholders
print("%s tem %d anos e ganha R$ %.2f reais por mês." %(name, age, salary))

#Outra opção para arredondar
print("Fulano ganha R$"+"{:.2f}".format(salary))

#Mais opções de formatação
print("O funcionário {:s}, sexo {:s}, idade {:d}, ganha {:.2f} reais.".format(name,gender,age,salary))


#Exemplos de Input
name1 = input("Digite um nome: ")
age1 = int(input("Digite a idade da pessoa: "))

print(f"{name1} tem {age1} anos")