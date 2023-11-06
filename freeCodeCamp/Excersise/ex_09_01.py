fname = input('Enter file: ')
if len(fname) < 1 : fname = 'Files/clown.txt'
hand = open(fname)

di = dict()

for lin in hand:
  lin = lin.rstrip()
  # print(lin)
  wds = lin.split()
  # print(wds)
  for w in wds:
    if w in di :
      di[w] = di[w] + 1
      print("**EXISTE**")
    else:
      di[w] = 1
      print('**NOVO**')
    print(w,di[w])