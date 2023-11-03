# isolar os numeros e transforma-los em float

str = 'X-DSPAM-Confidence: 0.8475'

# ipos = str.find(':')
# print(ipos)

# piece = str[ipos+2:]
# print(piece)

# value = float(piece)
# print(value)


def value():
  ipos = str.find(':')
  piece = str[ipos + 2:]
  value = float(piece)
  return value


resultado = value()

print(resultado)
