import random

# Definindo constantes para o jogo
NUM_DIGITS = 3  # Número de dígitos do número secreto
MAX_GUESSES = 10  # Número máximo de tentativas do jogador

def main():
    # Instruções do jogo
    print('''Bagels, um jogo de lógica dedutiva.
  
    Estou pensando em um número de {} dígitos sem dígitos repetidos.
    Tente adivinhar o que é. Aqui estão algumas pistas:
    Quando eu digo: Isso significa:
    Pico           Um dígito está correto, mas na posição errada.
    Fermi          Um dígito está correto e na posição correta.
    Bagels         Nenhum dígito está correto.

    Por exemplo, se o número secreto for 248 e o seu palpite for 843, o
    as pistas seriam Fermi Pico.'''.format(NUM_DIGITS))

    while True:  # Loop principal do jogo
        # Gerando o número secreto
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Continuar pedindo um palpite válido
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # O jogador acertou o número, sair do loop
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        # Perguntar se o jogador quer jogar novamente
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    """Gera um número secreto composto por dígitos únicos."""
    numbers = list('0123456789')  # Lista de dígitos de 0 a 9
    random.shuffle(numbers)  # Embaralha a lista

    # Obtém os primeiros NUM_DIGITS dígitos para o número secreto
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Gera dicas com base no palpite e no número secreto."""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')  # Dígito correto na posição correta
        elif guess[i] in secretNum:
            clues.append('Pico')  # Dígito correto na posição errada
    if len(clues) == 0:
        return 'Bagels'  # Nenhum dígito correto
    else:
        clues.sort()  # Ordena as dicas
        return ' '.join(clues)  # Junta as dicas em uma string

# Executa o jogo se o script for o principal executado
if __name__ == '__main__':
    main()
