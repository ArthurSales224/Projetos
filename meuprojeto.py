from datetime import datetime
import mysql.connector
import requests

try:
    con = mysql.connector.connect(host='localhost', database='banco', user='root', password='senha')
    cursor = con.cursor() 

    def adicionar_moeda():
        nome = input("Digite o nome da moeda: ")
        sigla = input("Digite a sigla da moeda (ex: BTC, ETH): ")
        preco = float(input("Digite o preço atual da moeda: "))

        sql = "INSERT INTO moedas (nome, sigla, preco_atual) VALUES (%s, %s, %s)"
        valores = (nome, sigla, preco)
        cursor.execute(sql, valores)
        con.commit()
        
        print(f"\n✅ Moeda {nome} adicionada com sucesso!\n")


    def listar_moedas():
        sql = "SELECT * FROM moedas"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        
        if resultados:
            print("\n📋 Moedas cadastradas:")
            print("-" * 40)
            for moeda in resultados:
                id, nome, sigla, preco = moeda
                print(f"ID: {id} | Nome: {nome} | Sigla: {sigla} | Preço Atual: R$ {preco:.2f}")
            print("-" * 40)
        else:
            print("\n⚠️ Nenhuma moeda cadastrada ainda.\n")

# Dicionário de siglas para nomes de moedas (CoinGecko)
    sigla_para_nome = {
        'BTC': 'bitcoin',
        'ETH': 'ethereum',
        'XRP': 'ripple',
        'LTC': 'litecoin',
        'BCH': 'bitcoin-cash',
        'ADA': 'cardano',
        'DOT': 'polkadot',
        'DOGE': 'dogecoin',
        'SOL': 'solana',
        'MATIC': 'matic-network',
        'VIB': 'viberate',
        'SUI': 'sui',
        'ALPACA': 'alpaca-finance',
        # Adicione mais siglas conforme necessário
    }
    def obter_preco_moeda(sigla):
        nome_moeda = sigla_para_nome.get(sigla.upper())
        
        if nome_moeda:
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={nome_moeda}&vs_currencies=usd"
            response = requests.get(url)

            if response.status_code == 200:
                dados = response.json()
                if nome_moeda in dados:
                    return dados[nome_moeda]['usd']
                else:
                    print(f"⚠️ A moeda {sigla.upper()} não foi encontrada na resposta da API.")
                    return None
            else:
                print(f"❌ Erro ao consultar API para {sigla.upper()}. Status: {response.status_code}")
                return None
        else:
            print(f"⚠️ A sigla {sigla.upper()} não está no mapeamento!")
            return None

    def atualizar_todos_precos_api():
        # Consultar todas as moedas cadastradas no banco de dados
        cursor.execute("SELECT id, sigla FROM moedas")
        moedas = cursor.fetchall()

        if not moedas:
            print("\n⚠️ Nenhuma moeda cadastrada para atualizar.\n")
            return

        for id_moeda, sigla in moedas:
            # Obtemos o preço da moeda pela sigla
            novo_preco = obter_preco_moeda(sigla)

            if novo_preco:
                # Atualiza o preço no banco de dados
                sql = "UPDATE moedas SET preco_atual = %s WHERE id = %s"
                valores = (novo_preco, id_moeda)
                cursor.execute(sql, valores)
                con.commit()

                print(f"✅ {sigla.upper()} atualizado para $ {novo_preco:.2f}")
            else:
                print(f"⚠️ Não foi possível obter o preço para {sigla.upper()}.")

        print("\n🏁 Atualização de todas as moedas concluída!\n")

    def registrar_operacao():
        print("\nEscolha o tipo de operação:")
        print("1 - Comprar")
        print("2 - Vender")

        tipo_opcao = input("Escolha uma opção: ")

        if tipo_opcao not in ["1", "2"]:
            print("\n❌ Opção inválida! Tente novamente.")
            return

        tipo = "compra" if tipo_opcao == "1" else "venda"

        listar_moedas()
        id_moeda = int(input(f"Digite o ID da moeda para registrar a operação de {tipo}: "))
        quantidade = float(input("Digite a quantidade: "))
        preco_unitario = float(input(f"Digite o preço unitário de {tipo} da moeda: "))

        # Registrar a operação na tabela de operações
        sql_operacao = """
        INSERT INTO operacoes (tipo, quantidade, preco_unitario, id_moeda)
        VALUES (%s, %s, %s, %s)
        """
        valores_operacao = (tipo, quantidade, preco_unitario, id_moeda)
        cursor.execute(sql_operacao, valores_operacao)
        con.commit()

        # Atualizar a tabela de carteira
        cursor.execute("SELECT quantidade FROM carteira WHERE id_moeda = %s", (id_moeda,))
        resultado = cursor.fetchone()

        if resultado:
            # Se a moeda já existe na carteira
            saldo_atual = resultado[0]

            if tipo == "compra":
                novo_saldo = saldo_atual + quantidade
            elif tipo == "venda" and saldo_atual >= quantidade:
                novo_saldo = saldo_atual - quantidade
            else:
                print("\n❌ Saldo insuficiente para venda!")
                return

            # Atualiza a quantidade na carteira
            sql_carteira = "UPDATE carteira SET quantidade = %s WHERE id_moeda = %s"
            valores_carteira = (novo_saldo, id_moeda)
            cursor.execute(sql_carteira, valores_carteira)
        else:
            # Se a moeda não existe na carteira, cria um novo registro
            if tipo == "compra":
                sql_carteira = """
                INSERT INTO carteira (id_moeda, quantidade)
                VALUES (%s, %s)
                """
                valores_carteira = (id_moeda, quantidade)
                cursor.execute(sql_carteira, valores_carteira)
            else:
                print("\n❌ Não é possível vender uma moeda que não está na carteira!")
                return

        con.commit()

        print(f"\n✅ Operação de {tipo} registrada com sucesso!")


    def menu_principal():       #Mostrar menu de opções 
        while True:
            print("""
    ========= MENU =========
    1 - Adicionar moeda
    2 - Listar moedas
    3 - Atualizar preço da moeda
    4 - Registrar operações
    0 - Sair
    ========================
    """)
            opcao = input("Escolha uma opção: ")        #Pedir para que o usuário escolha a opção desejada

            if opcao == "1":            #Determina o que ocorre de acordo com a escolha da opção
                adicionar_moeda()
            elif opcao == "2":
                listar_moedas()
            elif opcao == "3":
                atualizar_todos_precos_api()
            elif opcao == "4":
                registrar_operacao()

            elif opcao == "0":
                print("\n👋 Saindo... Até mais!\n")
                break
            else:
                print("\n❌ Opção inválida! Tente novamente.\n")

    def main():     #Função princial, onde as outras funções serão chamadas
        menu_principal()

    main()
except mysql.connector.Error as erro:    #Caso o código dê erro, mostrar erro
    print(f"Erro ao executar comando: {erro}")
finally:
    if con.is_connected():      #Fechar conexão com banco de dados
        cursor.close()
        con.close()
        print("Conexão encerrada.")




