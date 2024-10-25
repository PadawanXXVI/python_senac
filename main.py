from conexao import abrir_conexao, fechar_conexao

def insere_usuario(con, cod, nome, cidade, data_cadastro):
    cursor = con.cursor()
    sql = "inser into usuario values (%s,%s,%s,%s)"
    cursor.excute(sql)
    cursor.close()
    con.commit()

def main():
    con = abrir_conexao("localhost", "root", "senac", "senac")
    insere_usuario(con,null,"Derli","default",now())
    fechar_conexaao(con)

if __name__ == "__main__":
    main()

