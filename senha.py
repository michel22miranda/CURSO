import hashlib

def initial():
    r = input ("qual senha?")
    p = input ("sua frase?")
    return r + "#" + p
    
def crypto(senha):
    x = hashlib.sha512(senha.encode('utf-8')).hexdigest()
    return x

def invert(penta):
    return penta[::-1]

if __name__=="__main__":
    while True:
        x = initial()
        print(crypto(x))
        print(invert(x))
        




    