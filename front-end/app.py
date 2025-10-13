import streamlit as s
import requests as r

# url da api do fastapi
API_URL = "http://127.0.0.1:8000/"

s.set_page_config(page_title="gerenciador de filmes", page_icon="🎬🎥")

s.title("🍟 gerenciador de filmes 🍟")

menu = s.sidebar.radio('Navegação', ["Catalogo"])

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