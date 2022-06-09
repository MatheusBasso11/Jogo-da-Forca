# Alunos: Leonardo Telles e Matheus Basso

from Main import iniciar, limpatela, cabecalho, chamaescolha, confereescolha, conferetentativa, confereletra
from Main import verificaresposta, avisoresposta, verificadica, menufinal, boneco
import os

iniciar('Jogo da Forca')
cabecalho()

desafiante = verificaresposta((input("Quem será o desafiante? ")))
while desafiante == False:
    avisoresposta(desafiante)
    desafiante = verificaresposta((input("Quem será o desafiante? ")))
    
competidor = verificaresposta((input("Quem será o competidor? ")))
while competidor == False:
    avisoresposta(competidor)
    competidor = verificaresposta((input("Quem será o competidor? ")))

limpatela()

palavra = verificaresposta(input("Insira a palavra chave: "))
while palavra == False:
    avisoresposta(palavra)
    palavra = verificaresposta(input("Insira a palavra chave: "))

dica1 = verificadica(input("Insira a dica 1: "))
while dica1 == False:
    print("Não pode deixar vazio")
    dica1 = verificadica(input("Insira a dica 1: "))

dica2 = verificadica(input("Insira a dica 2: "))
while dica2 == False:
    print("Não pode deixar vazio")
    dica2 = verificadica(input("Insira a dica 2: "))

dica3 = verificadica(input("Insira a dica 3: "))
while dica3 == False:
    print("Não pode deixar vazio")
    dica3 = verificadica(input("Insira a dica 3: "))

bibliotecadica = {'dica1' : dica1, "dica2" : dica2, "dica3" : dica3}
limpatela()

print("-"*5, "palavra chave","-"*5,)
secret ="*" * len(palavra)
print(" "* 8, secret)
print("")
print("A palavra tem  "+ str(len(secret)) + 'letras.')

# as variaveis
letra = ""
erros = 0 
tentativa =''
contadicas = 1
letranapalavra = [ ]
bancoletras = []
vencedor = ""
perdedor = ""

while secret != palavra:
    escolha = chamaescolha()
    if escolha == '1':
        letra = verificaresposta(input('escolha uma letra: ')) 
        while letra == False:
            avisoresposta(letra)
            letra = verificaresposta(input('escolha uma letra: '))         
    elif escolha == '2':
        if contadicas < 4:
            print('dica'+ str(contadicas)+":", (bibliotecadica['dica' + str(contadicas)]))
            contadicas = contadicas + 1
        else:
            print("Você ja usou todas as dicas")
        letra = verificaresposta(input('escolha uma letra: '))
        while letra == False:
            avisoresposta(letra)
            letra = verificaresposta(input('escolha uma letra: ')) 
    elif escolha == '3':
        tentativa = input("Qual é a palavra? ")
        print('')
        if tentativa == palavra:
            print("______________________________________________")
            print("|                 Parabéns!!!                |")
            print("|               -VOCÊ ACERTOU!-              |")
            print("|____________________________________________|")
            print(" *** A palavra era", palavra,"***")
            vencedor = "competidor: "+competidor
            break
        else:
            print("  -VOCÊ ERROU!-")
            print("**A palavra não é ", tentativa,"**")
            erros = erros + 1       
    if escolha != '3':
        print('')       
        if letra in bancoletras:
            print("Esta letra ja foi escolida!!")
        elif letra in palavra:
            print("--------!Acertou!-------")     
        else:
            print("-------xERROUx-------")
            erros = erros +1
        bancoletras.append(letra)

    secret = ""
    for i in palavra: 
        if i == letra:
            letranapalavra.append(i)
            secret = secret + letra
        elif i in letranapalavra:
            secret = secret + i
        else:
            secret = secret + '*'
    letra = ''
    tentativa = ''
    escola = ''
    print('')
    print("-"*5, "palavra chave","-"*5,)
    print(" " * 5 + secret)
    print (" erros: ", erros)
    boneco(erros)
    if erros == 5:
        vencedor = "desafiante: "+desafiante
        break
    
    if secret == palavra:
        vencedor = "competidor: "+competidor
        break
    input('')
    limpatela()
    print("-"*5, "palavra chave","-"*5,)
    print(" " * 5 + secret)
    print("")
    print("A palvra tem  "+ str(len(secret)) + 'letras.')
    print (" erros: ", erros)
    boneco(erros)
    
print(" _________________________________________")
print(" |                                       |")
print(" |             O JOGO ACABOU             |")
print(" |_______________________________________|")
print("")


if vencedor == desafiante:
    perdedor = "competidor: "+competidor
else:
    perdedor ="desafiante: "+ desafiante
hisrorico = "  Palavra:" + palavra + " |vencedor- " + vencedor + " |perdedor- " + perdedor
print("-Histórico desta partida:")
print(hisrorico)
arquivo = open("historico jogo.txt" , "r")
texto = arquivo.read()
print("-Partidas anteriores:")
print(texto)
arquivo.close()
arquivo = open("historico jogo.txt", "a")
arquivo.write(hisrorico + "\n")
arquivo.close()
menufinal = menufinal()
while menufinal == "Entrda errada!":
    print(menufinal)
    menufinal = menufinal()