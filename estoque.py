from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/extrato/{dtinicial}/{dtfinal}")
def extrato(dtinicial:int, dtfinal:int):
    return {"msg":"ok"}

@app.put("/credito/{codigo}/{quantidade}")
def credito(codigo:int, quantidade:int):
    conn = sqlite3.connect("/home/ijovem03/turma202402/database/estoque.db")
    cur = conn.cursor()

    cur.execute(""" INSERT INTO registro (id_produto, qtde, operacao) VALUES (?,?, 'CREDITO') """, ( codigo, quantidade,))
    conn.commit()
    conn.close()

    atualizar_credito(codigo, quantidade)
    
    return {"msg":"credito efetuado"}

@app.put("/debito/{codigo}/{quantidade}")
def debito(codigo:int, quantidade:int):
    conn = sqlite3.connect("/home/ijovem03/turma202402/database/estoque.db")
    cur = conn.cursor()

    cur.execute(""" INSERT INTO registro (id_produto, qtde, operacao) VALUES (?,?, 'DEBITO') """, ( codigo, quantidade,))
    conn.commit()
    conn.close()
    
    atualizar_debito(codigo, quantidade)

    return {"msg":"debito efetuado"}


def atualizar_credito(codigo:int, quantidade:int):
    conn = sqlite3.connect("/home/ijovem03/turma202402/database/estoque.db")
    cur = conn.cursor()

    cur.execute(""" UPDATE produto SET saldo = saldo + ? WHERE id = ? """, (quantidade,codigo))
    conn.commit()
    conn.close()
    return 0

def atualizar_debito(codigo:int, quantidade:int):
    conn = sqlite3.connect("/home/ijovem03/turma202402/database/estoque.db")
    cur = conn.cursor()

    cur.execute(""" UPDATE produto SET saldo = saldo - ? WHERE id = ? """, (quantidade,codigo))
    conn.commit()
    conn.close()
    return 0 