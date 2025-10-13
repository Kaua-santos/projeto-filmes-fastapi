from fastapi import FastAPI
import funcoes as f

# Rodar fastapi = python -m uvicorn api:app -- reload

# testar a s rotas fastapi 
# /docs > documentação Swagger 
# /redoc > documentção Redoc

app = FastAPI(title="gerenciador de filmes")

# GET > Pegar/listar 
# POST > Enviar/cadastrar
# PUT > Atualizar 
# DELETE > Deletetar

# api sempre retorna dados em JSON (chave: Valor)
@app.get("/")
def home():
    return {"mensagem": "Bom dia - Bem vindo ao gerenciador de filmes"}