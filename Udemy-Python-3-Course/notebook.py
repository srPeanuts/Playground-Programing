
player = ['Thomas', 'Shelby']
points = 33
age = 26

# print('last night, '+player+' scored '+str(points)+' points')
# print('last night,', player, 'scored', points, 'points')
# print(f'last night, {player} scored {points} points')

# print(f"He said his name is {player!r}")
# print(f"He said is name is {player[0]} {player[1]}")

# first_name = player.pop(0)
# last_name = player.pop()
# print(first_name)
# print(last_name)


my_list = ['one', 'two', 'three', 4, 5]

# print(my_list * 2)
# rev_list = my_list
# print(rev_list)
# rev_list.reverse()
# print(rev_list)


my_dict = {'k1': 100, 'k2': 200, 'k3': 300, 'k5':{'name': 'molly', 'age': 2}}

# my_dict['k6'] = 400
# print(my_dict)
# my_dict['k2'] = 'Novo valor'
# print(my_dict)
# print(my_dict['k4'])
# print(my_dict['k5']['name'])
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())                                # item() dá origem a tuples como return!


# my_file = open('Importante_Files/test.txt')           # ficheiro é aberto aqui mas tem de ser fechado
# print(my_file.read())
# conteudo = my_file.read()                             # lê o ficheiro todo de uma vez        (opção #1)
## conteudo_1 = my_file.readline()                      # lê a primeira linha                  (opção ##2)
## conteudo_2 = my_file.readline()                      # lê a segunda linha                   (opção ##2)
# my_file.close()                                       # ficheiro é fechado aqui !IMPORTANTE!
# print(conteudo)                                                                            # (opção #1)
# print(conteudo_1.rstrip())                                                                 # (opção ##2)
# print(conteudo_2.rstrip())                                                                 # (opção ##2)

# with open('Importante_Files/test.txt') as new_file:
#     for line in new_file:
#         print(line.rstrip())

# with open('Importante_Files/novo.txt', mode='w') as novo_file:          # vai escrever no ficheiro ou criar um ficheiro com o nome novo.txt
#     novo_file.write("linha um de comando\nLinha dois de comando\n")     # e vai escrever o texto dado

# with open('Importante_Files/test.txt', mode="a") as f:                  # abrir um ficheiro existente
#     f.write('\nNext Line')                                              # adicionar/append um nova linha de texto

dias = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
meses = [1,2,3,4,5,6,7,8,9,10,11,12]

