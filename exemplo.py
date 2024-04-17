from fastapi import FastAPI

app = FastAPI()

@app.get("/ola/{nome}/{idade}")
def ola(nome:str, idade:int):
    x = " ola " + nome + " sua idade " + str(idade) + " anos "
    return {"msg":x}

@app.post("/valeu")
def valeu():
    return {"msg":"ola"}

@app.put("/polosul")
def cor():
    return{"msg":"azul"}

@app.delete("/polonorte")
def numero():
    return{"msg":"100"}

@app.get("/somar/{x}/{y}")
def somar (x:int,y:int):
    return{"msg":x+y}

@app.post("/quadrado/{x}/{y}")
def quadrado (x:int,y:int):
    return{"msg":(x+y)**2}
