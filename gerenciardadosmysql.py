import mysql.connector

#Gerenciar dados no Mysql(Inserir,Selecionar,Deletar e Atualizar)

try:
    con = mysql.connector.connect(host='localhost', database='banco', user='usuario', password='senha') #Conexão com banco de dados
    cursor = con.cursor() #Criar cursor para executar as tarefas no banco de dados

#1. INSERT (Inserir dados)

    def insercao(tabela,colunas,valor1,valor2,valor3):
        inser = f"INSERT INTO {tabela} ({colunas}) VALUES(%s, %s, %s)"
        val = (valor1,valor2,valor3)
        cursor.execute(inser,val)
        con.commit()
        print("Inserido com sucesso!")
            
    #insercao("test","nome,categoria,preco","feijao","alimento",10)
    
#2. DELETE (Deletar dados)

    def deleter(tabela,id,numero_id): 
        delt = f"DELETE FROM {tabela} WHERE {id} = {numero_id}"
        cursor.execute(delt)
        con.commit()
        print("Deletado com sucesso")

    #Exemplo: deleter("test","id","1")

#3. UPDATE (Atualizar dados)   

    def atualizar_nome(tabela, campo_nome, novo_nome, onde_id, id_valor):
        sql = f"UPDATE {tabela} SET {campo_nome} = '{novo_nome}' WHERE {onde_id} = {id_valor}"
        cursor.execute(sql)
        con.commit()
        print("tabela atualizada com sucesso!")

    #Exemplo: atualizar_nome("test","nome","arroz","id","2")

#4. SELECT geral (mostrar tabela)

    def select_geral(tabela):
        sel = f"SELECT * FROM {tabela}"
        cursor.execute(sel)
        mostrar = cursor.fetchall()
        for produto in mostrar:
            print(produto)

    #Exemplo: select_geral("test")

#4.1. SELECT especifico(mostrar coluna da tabela)

    def select(coluna,tabela):
        sql = f"select {coluna} from {tabela}"
        cursor.execute(sql)
        mostrar = cursor.fetchall()
        for produto in mostrar:
            print(produto)
    #Exemplo: select("nome","test")

except mysql.connector.Error as erro:    #Caso o código dê erro, mostrar erro
    print(f"Erro ao executar comando: {erro}")
finally:
    if con.is_connected():      #Fechar conexão com banco de dados
        cursor.close()
        con.close()
        print("Conexão encerrada.")