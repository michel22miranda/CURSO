import qrcode

def gerarqrcode (x):
    img = qrcode.make(x)
    img.save("michael.png")

def link():
    img = qrcode.make("https://www.instagram.com/icoelho/")
    img.save("link.png")

def senhawifi():
    img = qrcode.make("ijovem2024")
    img.save("senha.png")





def receberdados ():
    nome = input("digite seu nome :")
    end = input("digite seu end :")
    telefone = input("digite seu telefone :")
    msg = input("digite uma msg :")

    a = "Nome = " + nome + "\n End = "  +end + "\nTelefone = " + telefone + "\n Msg = " + msg
    return a

    
if __name__=="__main__":
    m = receberdados()
    gerarqrcode(m)
    link()
    senhawifi()