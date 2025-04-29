import mysql.connector

try:
    con = mysql.connector.connect(host='localhost', database='teste', user='root', password='Zoruark21#')
    cursor = con.cursor() 

#1. INSERT (Inserir dados)

    def insercao(valor1,valor2):
        inser = "INSERT INTO tbl(nome,preco) VALUES(%s, %s)"
        val = (valor1,valor2)
        cursor.execute(inser,val)
        con.commit()
        print("Inserido com sucesso!")
            

#2. DELETE (Deletar dados)

    def deleter(IdProduto): 
        delt = "DELETE FROM tbl WHERE IdProduto = %s"
        value = (IdProduto,)
        cursor.execute(delt,value)
        con.commit()
        print("Deletado com sucesso")


#3. UPDATE (Atualizar dados)   

    def atualizar_nome(tabela, campo_nome, novo_nome, onde_id, id_valor):
        sql = f"UPDATE {tabela} SET {campo_nome} = %s WHERE {onde_id} = %s"
        cursor.execute(sql, (novo_nome, id_valor))
        con.commit()
        print("tabela atualizada com sucesso!")
    """atualizar_nome("tbl", "nome", "feijao", "IdProduto", 9)"""""


#4. SELECT geral (mostrar tabela)

    def select_geral(tabela):
        sel = f"SELECT * FROM {tabela}"
        cursor.execute(sel)
        mostrar = cursor.fetchall()
        for produto in mostrar:
            print(produto)
    """select_geral("tbl")"""


#4.1. SELECT especifico(mostrar coluna da tabela)

    def select(coluna,tabela):
        sql = f"select {coluna} from {tabela}"
        cursor.execute(sql)
        mostrar = cursor.fetchall()
        for produto in mostrar:
            print(produto)
    """select("nome","tbl")"""

except mysql.connector.Error as erro:    #Caso o código dê erro, mostrar erro
    print(f"Erro ao executar comando: {erro}")
finally:
    if con.is_connected():      #Fechar conexão com banco de dados
        cursor.close()
        con.close()
        print("Conexão encerrada.")