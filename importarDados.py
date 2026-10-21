import sqlite3
import csv

#Caminho para o banco SQLite
db_path = "db.sqlite3"

#Conecta ao banco
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

#Abre o CSV e insere os dados
with open("base_filmes.csv", newline="", encoding="utf-8") as csvfile:
    arquivo = csv.DictReader(csvfile)

    for linha in arquivo:
        nome_genero = linha["genero"].strip()

        #Verifica se o gênero já existe
        cursor.execute(
            "SELECT id FROM filmes_generos WHERE nome = ?",
            (nome_genero,)
        )
        resultado = cursor.fetchone()

        if resultado:
            genero_id = resultado[0]  #Reutiliza o gênero existente
        else:
            cursor.execute(
                "INSERT INTO filmes_generos (nome) VALUES (?)",
                (nome_genero,)
            )
            genero_id = cursor.lastrowid  #Cria novo gênero

        #Insere o filme
        cursor.execute("""
            INSERT INTO filmes_filmes
            (titulo, descricao, ano_lancamento, genero_id, duracao)
            VALUES (?, ?, ?, ?, ?)
        """, (
            linha["titulo"].strip(),
            linha["descricao"].strip(),
            int(linha["ano_lancamento"]),
            genero_id,
            int(linha["duracao"])
        ))

#Salva e fecha a conexão
conn.commit()
conn.close()

print("Importação de filmes concluída com sucesso!")