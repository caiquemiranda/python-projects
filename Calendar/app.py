import datetime

# Importa o módulo datetime, que fornece funções e classes para trabalhar com datas e horas.

# Define constantes: DAYS é uma tupla contendo os nomes dos dias da semana; MONTHS é uma tupla com os nomes dos meses.
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday')

MONTHS = ('January', 'February', 'March', 
          'April', 'May', 'June',
          'July', 'August', 'September', 
          'October', 'November', 'December')

# Inicia um loop infinito para obter um ano válido do usuário.
while True:
    print('Enter the year for the calendar:')
    response = input('> ')

    # Pede ao usuário para inserir um ano.
    # Verifica se a resposta é um número decimal positivo. Se for, converte para inteiro e sai do loop.
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    # Caso contrário, pede ao usuário para inserir um ano numérico válido e continua o loop.
    print('Please enter a numeric year, like 2023.')
    continue

# Inicia outro loop infinito para obter um mês válido do usuário.
while True:
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    # Pede ao usuário para inserir um mês.
    # Verifica se a resposta é um número decimal. Se não for, pede um mês numérico válido e continua o loop.
    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    # Converte a resposta para um inteiro e verifica se está no intervalo de 1 a 12 (meses do ano). Se estiver, sai do loop.
    month = int(response)
    if 1 <= month <= 12:
        break

    # Caso contrário, informa ao usuário para inserir um número entre 1 e 12 e continua o loop.
    print('Please enter a number from 1 to 12.')


# Define a função getCalendarFor. Inicializa uma string vazia, calText, que conterá o calendário.
def getCalendarFor(year, month):
    calText = ''

    # Adiciona o nome do mês e o ano no topo do calendário. O nome do mês é obtido da tupla MONTHS.
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # Adiciona os nomes dos dias da semana ao calendário.
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # Define uma string que representa a linha horizontal separando as semanas.
    weekSeparator = ('+----------' * 7) + '+\n'

    # Define uma string para as linhas em branco dentro do calendário.
    blankRow = ('| ' * 7) + '|\n'

    # Cria um objeto datetime.date representando o primeiro dia do mês fornecido.
    currentDate = datetime.date(year, month, 1)

    # Retrocede a data até que o dia da semana seja domingo.
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    # Inicia um loop para cada semana do mês.
    while True:
        # Adiciona o separador de semana ao texto do calendário.
        calText += weekSeparator

        # Constrói a linha com os números dos dias, ajustando cada dia para a direita em dois espaços.
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            # Avança para o próximo dia.
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '|\n'  # Adiciona a linha vertical após o sábado.

        # Adiciona a linha dos números dos dias e três linhas em branco para cada semana no calendário.
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        # Verifica se o mês mudou (o que significa que o calendário do mês acabou) e sai do loop se verdadeiro.
        if currentDate.month != month:
            break

        # Adiciona a linha horizontal na parte inferior e retorna o texto do calendário.
        calText += weekSeparator
    return calText


# Chama a função getCalendarFor e imprime o calendário.
calText = getCalendarFor(year, month)
print(calText)  # Exibe o calendário.

# Cria um nome de arquivo baseado no ano e mês, e salva o texto do calendário nesse arquivo.
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

# Informa ao usuário que o calendário foi salvo no arquivo.
print('Saved to ' + calendarFilename)
