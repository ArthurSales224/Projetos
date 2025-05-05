import unicodedata

def eh_palindromo(texto):
    texto_limpo = texto.replace(" ", "").lower()
    reverso = texto_limpo[::-1]
    if texto_limpo == reverso:
        print("É palin")
    elif texto_limpo != reverso:
        print("Não é palin")

"""eh_palindromo("arara")"""

def contar_vogais(texto):
    texto = texto.lower()  # Converte tudo para minúsculo para ignorar maiúsculas
    contador = 0
    for char in texto:
        if char in "aeiou":  # Verifica se o caractere é uma vogal
            contador += 1
    return contador

# Testes:
"""print(contar_vogais("Python é massa"))  # 5
print(contar_vogais("ABC"))             # 1
print(contar_vogais("AEIOUaeiou"))"""      # 10

def extremos(lista):
    return (min(lista), max(lista))

# Testes:
"""print(extremos([4, 7, 1, 9, 3]))  # (1, 9)
print(extremos([10, 11, 13, 14])) # (10, 14)
print(extremos([100]))             # (100, 100)"""

def lista_nomes(lista):
    contagem = {}
    for nome in lista:
        nome_lower = nome.lower()  # Torna a contagem case-insensitive (opcional)
        if nome_lower in contagem:
            contagem[nome_lower] += 1
        else:
            contagem[nome_lower] = 1

    for nome, quantidade in contagem.items():
        print(f"Nome: {nome.capitalize()} | Quantidade: {quantidade}")

# Exemplo de uso
"""lista_nomes(["Pedro", "Raul", "Nicolas", "Andre", "Andre", "pedro"])"""

def list_nome(lista):
    nomes_unicos = []
    vistos = set()

    for nome in lista:
        chave = nome.lower()  # Chave para comparar sem considerar maiúsculas/minúsculas
        if chave not in vistos:
            nomes_unicos.append(nome)  # Mantém o nome original
            vistos.add(chave)

    nomes_ordenados = sorted(nomes_unicos, key=str.lower)
    print(f"Nomes: {nomes_ordenados}")



def remover_acentos(txt):
    return unicodedata.normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def validar_cadastro(idade, cidade):
    cidades_permitidas = ["rio de janeiro", "sao paulo", "belo horizonte"]
    nome_normalizado = remover_acentos(cidade.lower())

    if nome_normalizado not in cidades_permitidas:
        print("Cadastro recusado: cidade não permitida.")
    elif idade < 18:
        print("Cadastro recusado: menor de idade.")
    else:
        print("Cadastro aceito.")

def calcular_preco_final(preco,desconto):
    if desconto < 0 and desconto > 100:
        print("Desconto inválido")
    calcula_desconto = desconto / 100 * preco
    preco_final = preco - calcula_desconto
    return f"Preço final {preco_final:.2f}"
    

"""print(calcular_preco_final(13,54))"""

def somar_positivos():
    numeros_positivos = []
    while True:
        entrada = input("Digite um número (ou 'sair' para encerrar): ")
        
        if entrada.lower() == "sair":
            soma = sum(numeros_positivos)
            print(f"A soma dos números positivos é: {soma}")
            break

        try:
            numero = int(entrada)
            if numero > 0:
                numeros_positivos.append(numero)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro ou 'sair'.")


def analisa_frase(texto):
    texto_limpo = remover_acentos(texto.lower().strip())  # Remover acentos, tudo minúsculo e sem espaços extras
    contagem = texto_limpo.count("a")  # Contar as ocorrências da letra 'a'
    separa_palavra = texto_limpo.split()  # Separar a frase em palavras

    # Verificar se a primeira palavra começa com "ola"
    if separa_palavra[0] == "ola":
        print("A frase começa com 'olá'.")

    # Contar o número de palavras na frase
    num_palavras = len(separa_palavra)

    return {
        "Contagem da letra 'a'": contagem,
        "Número de palavras": num_palavras
    }

# Testando
frase = "  Olá, tudo bem? A Amanda adora abacaxi.  "
"""print(analisa_frase(frase))"""

def analisar_dados(kwargs):
    if "nome" not in kwargs:
        print("Nome não encontrado")
        return
    
    nome = kwargs["nome"]
    notas = kwargs["notas"]
    
    media = sum(notas) / len(notas)
    
    aprovado = "Aprovado" if media >= 7 else "Reprovado"
    
    cidade = kwargs.get("cidade", "Cidade não informada")  # Para garantir que "cidade" exista
    
    print(f"Nome: {nome}")
    print(f"Média das notas: {media:.2f}")
    print(aprovado)
    print(f"Cidade: {cidade}")

# Testando
dados = {
    "nome": "João",
    "idade": 18,
    "notas": [8.5, 7.0, 9.0, 6.5],
    "cidade": "São Paulo"
}

"""analisar_dados(dados)"""

def validar_entrada():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
        except ValueError:
            print("Erro: Valor não é um número inteiro")
            continue  # Pede novamente o número sem sair do loop

        email = input("Digite um e-mail: ")
        if "@" not in email or "." not in email:
            print("Erro: E-mail inválido")
            continue  # Pede novamente o e-mail sem sair do loop

        try:
            idade = int(input("Digite sua idade: "))
            if idade < 18:
                print("Erro: Idade inválida")
                continue  # Pede novamente a idade sem sair do loop
        except ValueError:
            print("Erro: Idade inválida")
            continue  # Pede novamente a idade sem sair do loop

        print(f"Número: {numero}, E-mail: {email}, Idade: {idade}")
        break  # Sai do loop quando tudo estiver válido

"""validar_entrada()"""

def cadastrar_usuario():
    while True:
        nome = input("Digite seu nome: ").strip()
        if not nome.isalpha():
            print("Erro: nome inválido. Digite apenas letras.")
            break  # ou return

        try:
            idade = int(input("Digite sua idade: "))
            if idade < 18:
                print("Cadastro recusado: menor de idade")
                break
        except ValueError:
            print("Erro: idade inválida")
            break

        cidade = input("Digite sua cidade: ")
        nome_limpo_cidade = remover_acentos(cidade.lower())
        cidades_permitidas = ["sao paulo", "rio de janeiro", "belo horizonte"]

        if nome_limpo_cidade not in cidades_permitidas:
            print("Cidade não permitida")
            break

        hobbies = input("Digite no máximo 5 hobbies, separados por vírgula: ").strip().split(",")
        hobbies = [h.strip() for h in hobbies if h.strip()]

        if len(hobbies) > 5:
            print("Limite de hobbies excedido (máx. 5)")
            break

    usuario = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "hobbies": hobbies
    }

    print("\n✅ Cadastro realizado com sucesso!")
    print(usuario)

print(sum([2, 4, 6, 8]))
list = [5, 10, 1, 7]
print(max(list),min(list))

nomes = ["python", "java", "c#"]
for i, nome in enumerate(nomes):
    print(f"linha{i}: {nome}")

name = ["Maria", "José"] 
notas = [7.5, 8.0]

for name,notas in zip(name,notas):
    print(f"{name} tirou {notas}")

