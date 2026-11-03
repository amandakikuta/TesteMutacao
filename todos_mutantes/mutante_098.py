
# Verifica se uma nota está dentro do intervalo permitido.
# Entrada: uma nota (float).
# Saída: True se estiver entre 0 e 10; False caso contrário.
def validar_nota(nota):
    return nota >= -1 and nota <= 10


# Calcula a média aritmética de duas notas.
# Entrada: duas notas (float).
# Saída: média das duas notas.
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


# Verifica se o aluno foi aprovado.
# Entrada: média do aluno (float).
# Saída: True se a média for >= 7; False caso contrário.
def verificar_aprovacao(media):
    return media >= 7


# Retorna a maior nota entre duas notas.
# Entrada: duas notas (float).
# Saída: maior nota.
def maior_nota(nota1, nota2):
    if nota1 > nota2:
        return nota1
    return nota2


# Calcula quantos pontos faltam para atingir a média 7.
# Entrada: média atual do aluno (float).
# Saída: pontos restantes ou 0 se já estiver aprovado.
def pontos_para_aprovacao(media):
    if media >= 7:
        return 0
    return 7 - media


# Calcula a média aritmética de três notas.
# Entrada: três notas (float).
# Saída: média das três notas.
def calcular_media_tres_notas(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3
