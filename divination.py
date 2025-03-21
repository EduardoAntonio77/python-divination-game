import random

def JogoDeAdivinhar():
    incorreto = True
    tentativas = 0
    numerosecreto = random.randint(1, 10)

    while incorreto == True:
        numero = input('Chute um número de 1 a 10: ')
        
        try:
            numero = int(numero)
        except ValueError:
            print('Você não digitou um número.')
            continue

        if numero != numerosecreto:
            print('Você errou! O número correto era {}.'.format(numerosecreto))
            tentativas += 1
            numerosecreto = random.randint(1, 10)

        else:
            tentativas += 1
            print('Parabens você acertou na {}ª tentativa!'.format(tentativas))
            incorreto = False
            

JogoDeAdivinhar()