
# Guessing Game (jogo dos 3 copos e da bola)
from random import shuffle

## função que da mix nos 'copos' onde está uma 'bola' escondida
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

## função que pergunta ao user por um numero e retorna, onde é guardada numa variavel
def player_guess():
    guess = ''
    #continua a perguntar até o user passar uma opção válida [0, 1 ou 2]
    while guess not in ['0','1','2']:
        guess = input('Pick an index: 0, 1 or 2 =>')
    return int(guess)

## função onde verifica a resposta do user com a função de mix de 'copos'
def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct')
    else:
        print('Wrong! Here is the correct index:')
        print(mylist)

#criada a lista onde o 'O' simboliza a bola, a unica resposta correta
mylist = [' ','O',' ']

# 1º mistura os copos e guarda numa variavel 'mixed_list'
mixed_list = shuffle_list(mylist)

# 2º pergunta pela escolha do user e guarda numa variavel 'guess'
guess = player_guess()

# 3º verifica a resposta do user na variavel 'guess' 
# com a opção correta no index correto da 'mixed_list'
check_guess(mixed_list,guess)