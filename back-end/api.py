from fastapi import FastAPI
import funcoes as f

# Rodar fastapi = python -m uvicorn api:app --reload

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

@app.get("/filmes")
def catalogo():
    filmes = f.listar_movies()
    lista = []
    for filme in filmes:
        lista.append( { "id": filme[0],
                        "titulo": filme[1],
                        "genero": filme[2],
                        "ano": filme[3],
                        "avaliação": filme[4] })
    return {"filmes": lista}

@app.post("/filmes")
# titulo, genero, ano, nota 
def adicionar_filmes(titulo : str, genero: str, ano: int, nota: float ):
    f.criar_fime(titulo,genero,ano,nota)
    return{"mensagem": "filme adicionado com sucesso"}

@app.put("/filmes/{id_filme}")
def atualizar_filmes(id_filme,nova_avaliacao: float):
    filme = f.buscar_movie(id_filme)
    if filme:
        f.atualizar_movies(id_filme, nova_avaliacao)
        return{"mensagem": "filme atualizado com sucesso"}
    else:
        return{"erro": "filme não encontrado"}
    
@app.delete("/filmes/{id_filme}")
def deletar_filme(id_filme: int):
    filme = f.buscar_movie(id_filme)
    if filme:
        f.deletar_movies(id_filme)
        return{"mensagem": "Filme deleteado com sucesso"}
    else:
        return{"erro": "filme não encontrado"}