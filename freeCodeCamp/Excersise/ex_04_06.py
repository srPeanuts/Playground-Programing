def computepay(hours, rate):
  #  print("In computepay", hours, rate)
  if hours > 40:
    reg = rate * hours
    otp = (hours - 40) * (rate * 0.5)
    pay = reg + otp
  else:
    pay = rate * hours
#  print("returning", pay)
  return pay


# PEDIR HORAS E RATE
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
# CONVERTER HORAS E RATE PARA FLOAT
fh = float(sh)
fr = float(sr)

xp = computepay(fh, fr)

# MOSTAR QUANTO É QUE TEM DE SER PAGO
print("Pay:", xp)
