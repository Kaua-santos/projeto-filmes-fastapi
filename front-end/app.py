import streamlit as s
import requests as r

# url da api do fastapi
API_URL = "http://127.0.0.1:8000/"

s.set_page_config(page_title="gerenciador de filmes", page_icon="🎬🎥")

s.title("🍟 gerenciador de filmes 🍟")

menu = s.sidebar.radio('Navegação', ["Catalogo", "Adicionar filme", "atualizar filme"])


if menu == "Catalogo":
    s.subheader("🎥 Todos os filmes 🎥")
    response = r.get(f"{API_URL}/filmes")
    if response.status_code == 200: 
        filmes = response.json().get("filmes",[])
        if filmes:
            for filme in filmes:
                s.write(f" **{filme['titulo']}** ({filme['ano']}) - {filme['genero']} - 🌟 {filme['avaliação']} ")
        else:
            s.info("nenhum filme encontrado")
    else:
        s.error("erro ao conectar com a API")

elif menu == "Adicionar filme":
    s.subheader('➕ Adicionar filme')
    titulo = s.text_input("titulo do filme")
    genero = s.text_input("Genero")
    ano = s.number_input("Ano de lançamento", min_value=1900, max_value=2100)
    avaliaçao = s.number_input("Avaliação de (0 a 10)", min_value=0, max_value=10, step=1)

    if s.button("Salvar filme"):
        params = {"titulo": titulo, "genero":genero, "ano": ano, "nota": avaliaçao}
        response = r.post(f"{API_URL}/filmes", params=params)
        if response.status_code == 200:
            s.success("filme adicionado com sucesso")
        else:
            s.error("Erro ao adicionar o filme")
    
elif menu == "atualizar filme":
    s.subheader("atualizar filme")
    id_filme = s.number_input("ID do filme a atualizar", min_value= 1, step= 1)
    nova_avaliação = s.number_input("Nova Avalição", min_value= 0, max_value= 10)
    if s.button("Atualizar"):
        dados = {"nova_avaliacao": nova_avaliação}
        response = r.put (f'{API_URL}/filmes/{id_filme}', params=dados)
        if response.status_code == 200:
            data = response.json()
            if "erro" in data: 
                s.warning(data["erro"])
            else:
                s.success("Filme atualizado com sucesso 😁👍")
        else:
            s.error("erro ao atualizar filme ❌")





    