from fastapi import FastAPI

app = FastAPI()

@app.post("/inserir/{nome}/{fabricante}/{descricao}")
def inserir(nome:str, fabricante:str, descricao:str):
    return{"msg":"inserido o produto"}

@app.put("/alterar/{id}/{nome}/{fabricante}/{descricao}")
def alterar(id:int, nome:str, fabricante:str, descricao:str):
    return{"msg":"alterado com sucesso"}

@app.put("/cancelar/{id}")
def cancelar(id:int):
    return{"msg":"cancelado o registro"}