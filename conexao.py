import mysql.connector

def abrir_conexao(host, usuario, senha, banco):
    return mysql.connector(host=host,user=usuario,password=senha,database=banco)

def fechar_conexao(con):
    return con.close()
    