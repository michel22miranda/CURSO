from fastapi import FastAPI

app = FastAPI()

@app.post("/registrar_credito/{cod_produto}/{qtde}/{data}")
def credito(cod_produto:str, qtde:int, data:int):
    return{"msg":"credito feito com sucesso"}

@app.post("/registrar_debito/{cod_produto}/{qtde}/{data}")
def debito(cod_produto:str, qtde:int, data:int):
    return{"msg":"debito feito com sucesso"}

@app.get("/extrato/{data_inicial}/{data_final}")
def extrato(data_inicial:int, data_final:int):
    return{"msg":"extrato concluido"}



