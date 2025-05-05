"""sequencia[início:fim:passo]
    início: índice inicial (inclusive)
    fim: índice final (exclusive)
    passo: de quantos em quantos vai andar"""

texto = "python"
reverso = texto[::-1]


lista = [1, 2, 3, 4]
"""print(lista[::-1]) """ # saída: [4, 3, 2, 1]

texto = "abcdefg"

#Expressão	Resultado	Explicação

texto[0:3]	#'abc'	    Do índice 0 até antes do 3
texto[2:]	#'cdefg'	Do índice 2 até o final
texto[:4]	#'abcd'	    Do início até antes do índice 4
texto[::2]	#'aceg'	    De 2 em 2
texto[::-1]	#'gfedcba'	Inverte a string
texto[1:6:2] #'bdf'	    Do índice 1 ao 5, de 2 em 2

numeros = [10, 20, 30, 40, 50, 60, 70]

#Expressão	Resultado	                           Explicação

numeros[:3]	#[10, 20, 30]	                    3 primeiros elementos
numeros[::2]  #[10, 30, 50, 70]	                Um sim, um não
numeros[::-1] #[70, 60, 50, 40, 30, 20, 10]	    Inverso da lista
numeros[-3:]  #[50, 60, 70]	                    Últimos 3 elementos
numeros[1:-1]  #[20, 30, 40, 50, 60]	        Ignora o primeiro e o último

numeros = [10, 20, 30, 40, 50, 60, 70]
# índices:  0   1   2   3   4   5   6
# negativos: -7 -6 -5 -4 -3 -2 -1

#Quando você faz:
numeros[1:-1]
#Começa no índice 1 → valor 20
#Vai até o índice -1, mas não o inclui (isso é importante!)
#Ou seja: vai do índice 1 até antes do último (índice -1 → valor 70)

#👉 Resultado: [20, 30, 40, 50, 60]
#🔍 Ele "ignora" o último porque o fim no slicing não é incluído.

#📌 2. Por que numeros[::-1] não ignora o último?
#Esse é o slicing invertido, então:

numeros[::-1]
#Significa: "Pegue tudo de trás para frente, um por um"

#Como você não especificou início nem fim, ele começa do final da lista e vai até o início.

#👉 Resultado: [70, 60, 50, 40, 30, 20, 10]

#📌 3. Por que numeros[-3:] começa do 50?
#Relembrando os índices negativos:

numeros = [10, 20, 30, 40, 50, 60, 70]
# índices:  0   1   2   3   4   5   6
# negativos: -7 -6 -5 -4 -3 -2 -1
#-3 aponta para o valor 50

#: sozinho até o fim → vai até o final da lista

#👉 Resultado: [50, 60, 70]
#✅ Começa do 50 porque esse é o valor no índice -3

def soma_total(*numeros):
    soma = sum(numeros)
    return soma



def info_pessoa(**dados):
    for nome,idade, in dados.items():
        print(f"{nome}: {idade}")

def mostrar_info(**dados):
    total = len(dados)
    campos = ", ".join(dados.keys())

    print(f"Total de dados: {total}")
    print(f"Campos recebidos: {campos}")

"""mostrar_info(nome="João", idade=25, cidade="SP")"""

#Criar uma única string com os nomes dos campos (as chaves do dicionário), separados por vírgulas.

#✅ Etapa por etapa:
#🔹 dados.keys()
#dados é um dicionário vindo do **kwargs

#.keys() retorna todas as chaves do dicionário

dados = {'nome': 'João', 'idade': 25, 'cidade': 'SP'}
dados.keys()  # → dict_keys(['nome', 'idade', 'cidade'])
#🔹 ", ".join(...)
#join() é um método de string que junta todos os elementos de uma lista/iterável em uma única string, usando o texto que está antes do .join() como separador

lista = ['nome', 'idade', 'cidade']
", ".join(lista) 
# nome: João
# idade: 25

def exibir(*args,**kwargs):
    print(f"Args: {args}")
    print("Kwargs:")
    for chave,valor in kwargs.items():
        print(f"{chave}: {valor}")

"""exibir(1,2,3,Nome="Ana",Ativo=True)"""

def multiplicar(val, *args):
    resultado = val
    for num in args:
        resultado *= num
    return resultado

# Testes:
"""print(multiplicar(2, 3, 4))     # 2 * 3 * 4 = 24
print(multiplicar(5))           # 5
print(multiplicar(1, 2, 3, 0))  """# 0

        
def filtrar_string(**dados):
    for chave,val in dados.items():
        if type(val) == str:
            print(f"{chave}: {val}")

"""filtrar_string(nome="Ana",bebe="Douglas",besbe=39)"""

def somar_numero(*args):
    soma = 0
    for numero in args:
        if isinstance(numero, (int, float)) and not isinstance(numero, bool):
            soma += numero
    return soma

"""print(somar_numero(1, 2, "a", [4], 3.5))  # Saída: 6.5"""

def contar_flags(**kwargs):
    contador_true = 0
    contador_false = 0
    for valor in kwargs.values():
        if valor is True:
            contador_true += 1
        elif valor is False:
            contador_false += 1
    return {"True": contador_true, "False": contador_false}

# Testando a função
"""resultado = contar_flags(ativo=True, admin=False, caca=True, ppe=False, logado=True, nome="Ana")
print(resultado)"""

# Saída esperada: 2
def somar_numeros(**kwargs):
    soma = 0
    for valor in kwargs.values():
        if isinstance(valor,(int,float)) and not isinstance(valor,bool):
            soma += valor
    return soma
    
"""resultado = somar_numeros(a=10, b="teste", c=5.5, d=3, e=True, f=[1, 2])
print(resultado)"""

def organizar_pares_impares(lista):
    pares = []
    impares = []
    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    return {"pares": pares, "ímpares": impares}

# Teste


def contar_palavras(texto):
    texto_limpo = texto.lower()
    repl = texto_limpo.replace(",", "").replace("!", "").replace(".", "")
    palavras = repl.split()

    total = len(palavras)
    unico = len([p for p in palavras if palavras.count(p) == 1])

    # Contagem das palavras específicas
    contagem = {
        "ola": palavras.count("olá"),
        "mundo": palavras.count("mundo"),
        "python": palavras.count("python"),
        "lindo": palavras.count("lindo"),
        "vasto": palavras.count("vasto")
    }

    return {"total": total, "unico": unico, "contagem": contagem}



def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia



def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado




def cadastrar_usuario(*args, **kwargs):
    # Verifica se o campo 'nome' foi passado
    if "nome" not in kwargs:
        print("Erro: O campo nome é obrigatório.")
        return

    # Verifica se nome é uma string
    if not isinstance(kwargs["nome"], str):
        print("Erro: 'nome' deve ser uma string.")
        return

    # Verifica se idade existe e é um inteiro
    if "idade" in kwargs and not isinstance(kwargs["idade"], int):
        print("Erro: 'idade' deve ser um número inteiro.")
        return

    # Verifica se todos os hobbies são strings
    for hob in args:
        if not isinstance(hob, str):
            print("Erro: todos os hobbies devem ser strings.")
            return

    # Limita os hobbies a 5
    if len(args) > 5:
        print("Aviso: número máximo de 5 hobbies permitidos. Os extras foram ignorados.")
        args = args[:5]

    # Imprime os dados
    print("\n📋 Cadastro do Usuário:")
    for chave, valor in kwargs.items():
        print(f"{chave.capitalize()}: {valor}")

    print("\n🎯 Hobbies:")
    for hob in args:
        print(f"- {hob}")





        

