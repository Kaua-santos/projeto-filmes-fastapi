from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS movies (
                    id SERIAL PRIMARY KEY ,
                    titulo TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    ano INTEGER NOT NULL,
                    avaliacao REAL
                    )
                """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.close()

criar_tabela()


def criar_fime(titulo,genero,ano,avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO movies (titulo,genero,ano,avaliacao)  VALUES (%s, %s,%s,%s)",
                (titulo,genero,ano,avaliacao)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir filme {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_movies():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM movies ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar filmes {erro}")
            return[]
        finally:
            cursor.close()
            conexao.close()


def atualizar_movies(id_filme,nova_avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE movies SET avaliacao= %s WHERE id = %s",
                (nova_avaliacao, id_filme)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar nota do filme:  {erro}")
        finally:
            cursor.close()
            conexao.close()



def deletar_movies(id_filmes,):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM movies WHERE id = %s", (id_filmes,)
            
            )
            conexao.commit()
        except Exception as erro:
            print(f'erro ao deletar filme: {erro} ')
            cursor.close()
            conexao.close()

def buscar_movies(nome_filme):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                
            )
        except Exception as erro:
            print(f"filme nao encontrado {erro}")

busca = buscar_movies("como treinar seu dragao")
print(busca)