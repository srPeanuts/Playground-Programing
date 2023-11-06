
# PEDIR HORAS E RATE
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

# CERTIFICAR QUE O INPUT SÃO NUMEROS 
# CONVERTER HORAS E RATE PARA FLOAT
try:
  fh= float(sh)
  fr= float(sr)
except:
  print("Error, please enter numeric input")
  quit()

# CALCULAR O OVERTIME
if fh > 40 :
  reg=fr*fh
  otp=(fh-40)*(fr*0.5)
  xp=reg+otp
else:
  xp=fr*fh

# MOSTAR QUANTO É QUE TEM DE SER PAGO
print("Pay:",xp)
