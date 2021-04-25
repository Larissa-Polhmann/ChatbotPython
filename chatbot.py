import os

def processar_resposta(resposta,nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, nossa clínica está aberta de segunda à sexta das 7:00 às 21h para consultas eletivas{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, temos especialistas em ortopedia, pediatria, ginecologia e cardiologia{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, possuímos pronto atendimento 24h apenas para ortopedia em todos os dias da semana{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, aceitamos os seguintes planos de saúde: Amil, Bradesco Saúde e Sul América{os.linesep}')
    else:
        print(f'{os.linesep}Digite apenas 1, 2, 3 ou 4{os.linesep}')

def start():
    #Início do chat
    print('Olá!! Bem-vindo(a) a nossa clínica!!')
    
    #Digitar nome
    nome = input('Digite seu nome: ')
    
    #Digitar email
    email = input('Digite seu e-mail: ')
    
    while True:
        #menu de opções
        resposta = input(f'{os.linesep}Qual a sua dúvida?{os.linesep}{os.linesep}[1] - Qual o horário de funcionamento?{os.linesep}[2] - Quais especialidades vocês atendem?{os.linesep}[3] - Vocês possuem pronto atendimento?{os.linesep}[4] - Aceitam plano de saúde?{os.linesep}')
        
        #processar a resposta
        processar_resposta(resposta,nome)


if __name__ == '__main__':
    start()