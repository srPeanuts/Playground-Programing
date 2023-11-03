# variaveis
num = 0
total = 0

# inicio de input de numeros e saida do loop
while True:
  sval = input("Enter a number: ")
  if sval == "done":
    break
# verifica se é um numero
  try:
    fval = int(sval)
  except ValueError:
    print("Invalid input!")
    continue
# adiciona às variaveis
  num += 1
  total = total + fval

print(total, num, total / num)
