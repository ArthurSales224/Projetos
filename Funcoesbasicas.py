soma = 0
quantidade = 0

with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        nome, nota = linha.strip().split()
        print(f"{nome} tirou {nota}")
        soma += float(nota)
        quantidade += 1

media = soma / quantidade
"""print(f"Média da turma: {media:.2f}")"""

numeros_pares = []
for i in range(1,101):
    if i % 2 == 0:
        numeros_pares.append(i)
"""print(sum(numeros_pares))"""

lista_nomes = ["ana", "bia", "carlos"]
for i,nome in enumerate(lista_nomes):
    """print(f"Posição{i}: {nome}")"""

nomes = ["Ana","Maria","João"]
notas = [8.5,9.0,7.0]


"""for nome,nota in zip(nomes,notas):
    print(f"{nome} tirou {nota}")"""

soma = 0
quantidade_notas = len(notas)
soma = sum(notas)
media = soma / quantidade
"""print(f"A média da turma foi {media:.2f}")"""

def eh_par(numero):
    return numero % 2 == 0


"""print(eh_par(3))"""

numeros = [1, 2, 3, 4]
dobro = list(map(lambda x: x * 2, numeros))
"""print(dobro)  # [2, 4, 6, 8]"""

numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
"""print(pares)  # [2, 4, 6]"""

nomes_2 = ["ana", "joão", "bia", "carlos"]
arruma_lista = list(map(lambda p: p.capitalize(),nomes_2))
"""print(arruma_lista)"""

nomes_3 = ["ana", "joão", "bia", "carlos", "leo", "fernando"]
quatro_letras = list(filter(lambda p: len(p)<= 4,nomes_3))
"""print(quatro_letras)"""

pessoas = [("Ana", 25), ("Carlos", 30), ("João", 20), ("Bia", 18)]
ordenacao = sorted(pessoas,key=lambda p: p[0])
"""print(ordenacao)"""

pessoas_1 = {
    "Ana": 25,
    "Carlos": 30,
    "João": 20,
    "Bia": 18
}
ordem_mais_velho = sorted(pessoas_1.items(),key=lambda p: p[1],reverse=True)
"""print(ordem_mais_velho)"""

quadrados = [x**2 for x in range(0,21,2)]
"""print(quadrados)"""

palavras = ["python", "java", "javascript", "c", "kotlin", "go", "typescript"]
palavras_4 = [palavra for palavra in palavras if len(palavra) > 5]
"""print(palavras_4)"""

numeros = [3, -1, 4, -7, 2, -9, 5]
numeros_negativos = [numero for numero in numeros if numero < 0]
"""print(numeros_negativos)"""

numeros_1 = [1, 2, 3, 4, 5]
numeros_3 = [numero*3 for numero in numeros_1]
"""print(numeros_3)"""

numeros_4 = [12, 15, 20, 25, 30, 35, 40, 45]
numeros_impares = [impar for impar in numeros_4 if impar % 2 != 0]
"""print(numeros_impares)"""


def soma_num(n):
    soma = 0
    for i in range(1,n+1):
        soma += i
    return soma

"""print(soma_num(3))"""

def inverte_string(palavra):
    inverso = palavra[::-1]
    return inverso

"""print(inverte_string("python"))"""

def palindromo(palavra):
    inverso = inverte_string(palavra)
    if inverso == palavra:
        print("É palíndromo")
    else:
        print("Não é palíndromo")
"""palindromo("osso")"""

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
"""print(eh_primo(15))"""



def remover_duplicatas(lista):
    unico = []
    for i in lista:
        if i not in unico:
            unico.append(i)
    return unico

# Testes
print(remover_duplicatas([1, 2, 1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]
print(remover_duplicatas(["a", "b", "a", "c"]))     # ["a", "b", "c"]

