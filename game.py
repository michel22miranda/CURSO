import sys
import os
import random
def menu ():
    print("0 = sair")
    print("1 = mega sena")
    print("2 = lotofacil")
    print("3 = gerar senha")
    r=int(input("qual o jogo?"))
    return r

def megasena ():
    os.system("clear")
    print ("megasena")
    r=int(input("quantos jogos?"))
    for j in range (r):
        numeros=""
        for n in range (6):
            x = random.randrange(1,60+1)
            numeros= numeros + str(x) + " "
        print (f"jogo {j+1} : {numeros} ")
    p = input ("ENTER p/ novo jogo")
    os.system("clear")

def lotofacil():
    os.system("clear")
    print ("lotofacil")
    r=int(input("quantos jogos?"))
    for j in range (r):
        numeros=""
        for n in range (15):
            x = random.randrange(1,25+1)
            numeros= numeros + str(x) + " "
        print (f"jogo {j+1} : {numeros} ")
    p = input ("ENTER p/ novo jogo")
    os.system("clear")

def senha():
    #os.system("clear")
    print ("password")
    numeros=""
    os.system("clear")
    for n in range(6):
        x = random.randrange(1,10)
        numeros= numeros + str(x) + ""
    print (f"senha : {numeros} ")
    p = input ("ENTER p/ nova senha")
    os.system("clear")
    


if __name__=="__main__":
    while True:
        r=menu()
        if r==0:
            sys.exit()
        if r==1:
            megasena()
        if r==2:
            lotofacil()
        if r==3:
            senha()
