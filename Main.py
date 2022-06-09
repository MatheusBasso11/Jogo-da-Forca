import os
def iniciar(titulo):
    import os
    os.system('cls')
    os.system('title ' + titulo)

def limpatela():
    import os
    os.system('cls')

def cabecalho():
    print(" ")
    print("                                       ")
    print("              Jogo da Forca            ")
    print(" ")
    print("")

def verificaresposta(resposta):
    if resposta == '':
        resposta = False
    else:
        for i in resposta:
            try:
                numero = int(i)
                resposta = False
            except:
                resposta = resposta
    return resposta

def avisoresposta(resposta):
    if resposta == False:
        print("entrada invalida!")
        print("Não pode deixar vazio e nem colocar número")
        
def verificadica(dica):
    if dica == '':
        dica = False
    else:
        dica = dica
    return dica

def chamaescolha():
    escolha = input("Deseja jogar(1), solicitar dica(2) ou falar a resposta(3)? ")
    while escolha != "1" and escolha != '2' and escolha != '3':
        print("Não temos esta opção")
        escolha = input("Deseja jogar(1), solicitar dica(2) ou falar a resposta(3)? ")
    return escolha

def confereescolha(escolha, biblioteca,verificaresposta, avisoresposta, contadicas,tentativa):
    if escolha == '1':
        letra = verificaresposta(input('escolha uma letra: '))  
        while letra == False:
            avisoresposta(letra)
            letra = verificaresposta(input('escolha uma letra: '))         
    elif escolha == '2':
        if contadicas < 4:
            print('dica'+ str(contadicas)+":", (biblioteca['dica' + str(contadicas)]))
            contadicas = contadicas + 1
        else:
            print("Você ja usou todas as dicas")
        letra = verificaresposta(input('escolha uma letra: '))
        while letra == False:
            avisoresposta(letra)
            letra = verificaresposta(input('escolha uma letra: ')) 
    elif escolha == '3':
        tentativa = input("Qual é a palavra? ")

def conferetentativa(tentativa, palavra, erros, secret):
    if tentativa == palavra:
        print("Parabéns!!!")
        print("Você acertou a palavra era ", palavra)
        secret = palavra
    else:
        print("Você errou!")
        print("A palavra não é ", tentativa)
        erros = erros + 1

def confereletra(letra, palavra, erros, bancoletras):
    if letra in bancoletras:
        print("Esta letra ja foi escolida!!")
    elif letra in palavra:
        print("--------!Acertou!-------")     
    else:
        print("-------xERROUx-------")
        erros = erros +1
    bancoletras.append(letra)

def menufinal():
    menufinal = input('Começar novo jogo(1) ou Fechar jogo(2): ')
    if menufinal == '1':
        os.system("cls")
        os.system("jogoforca.py")
    elif menufinal == '2':
        return os.system("cls")
    elif menufinal == "limpar historico":
        arquivo = open("banco.txt", "w")
    else:
        return "Entrda errada!"

def boneco(erros):
    if erros == 1:
        print("""_______________
|             |
|             Ô
|             |
|            
|""")
    elif erros == 2:
        print("""_______________
|             |
|             Ô
|            /|
|            
|""")
    elif erros == 3:
        print("""_______________
|             |
|             Ô
|            /|\\
|            
|""")
    elif erros == 4:
        print("""_______________
|             |
|             Ô
|            /|\\
|            / 
|""")
    elif erros == 5:
        print("""_______________
|             |
|             Ô
|            /|\\
|            / \\
|""")