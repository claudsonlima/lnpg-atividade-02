def ler(path):
    arquivo  = open(path, 'r', encoding='utf-8')
    return arquivo.read()

def palavras(texto):
    caracteres_especiais = '."(*$;.,;'
    for caractere in texto:
        if(caractere in caracteres_especiais):
            texto = texto.replace(caractere, '')

    return texto.lower().split()

def vogal(texto):
    vogais = ['a', 'e', 'i', 'o', 'u']
    apararicoes_por_vogal = []
    for vogal in vogais:
        aparicoes = texto.count(vogal)
        apararicoes_por_vogal.append(aparicoes)
    
    maior_aparicao = max(apararicoes_por_vogal)

    return vogais[apararicoes_por_vogal.index(maior_aparicao)]

def maiores_palavras(texto):

    texto = set(palavras(texto))

    palavra_por_tamanho = []
    cinco_maiores = []

    for palavra in texto:
        tamanho_palavra = len(palavra)
        palavra_por_tamanho.append((tamanho_palavra, palavra))

    palavra_por_tamanho = sorted(palavra_por_tamanho, reverse= True)

    for i in range(5):
        cinco_maiores.append(palavra_por_tamanho[i])

    return cinco_maiores


def literal(texto):
    arquivo = open(texto, 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    string = 'ção'
    linha = ''

    for i in range(len(linhas)):
        if(string in linhas[i]):
            linha = i + 1
            break

    if(linha == ''):
        return 'Literal não encontrado'
    else:
        return linha

path = input()
texto = ler(path)

qtd_palavras = len(palavras(texto))
cinco_maiores = maiores_palavras(texto)
apacicao_vogal = vogal(texto)
buscar_literal = literal(path)

print(f'#1 - {qtd_palavras}\n#2 - {cinco_maiores}\n#3 - {apacicao_vogal}\n#4 - {buscar_literal}')