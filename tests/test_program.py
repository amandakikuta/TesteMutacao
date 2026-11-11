from codigo.program import (
    validar_nota,
    calcular_media,
    verificar_aprovacao,
    maior_nota,
    pontos_para_aprovacao,
    calcular_media_tres_notas
)

# ============== + validar_nota + ==============

def test_validar_nota_limite_superior():
    assert validar_nota(10) == True

def test_validar_nota_limite_inferior():
    assert validar_nota(0) == True

def test_validar_nota_acima():
    assert validar_nota(11) == False

def test_validar_nota_negativo():
    assert validar_nota(-1) == False

# ============== + calcular_media + ==============

def test_calcular_media_10():
    assert calcular_media(10, 10) == 10

def test_calcular_media_quebrado():
    assert calcular_media(10, 7) == 8.5
    
# =========== + verificar_aprovacao + ===========

def teste_verificar_aprovacao():
    assert verificar_aprovacao(6.9) == False

def teste_verificar_aprovacao_10():
    assert verificar_aprovacao(10) == True

def teste_verificar_aprovacao_limite():
    assert verificar_aprovacao(7) == True

# ============== + maior_nota + ==============

def test_maior_nota():
    assert maior_nota(6, 6.1) == 6.1

def test_maior_nota_nota1():
    assert maior_nota(6.1, 6) == 6.1

def test_maior_nota_igual():
    assert maior_nota(6, 6) == 6

# ========= + pontos_para_aprovação + =========

def test_pontos_para_aprovacao_limite():
    assert pontos_para_aprovacao(7) == 0

def test_pontos_para_aprovacao_abaixo():
    assert pontos_para_aprovacao(3) == 4

def test_pontos_para_aprovacao_quebrado():
    assert pontos_para_aprovacao(3.5) == 3.5

def test_pontos_para_aprovacao_acima():
    assert pontos_para_aprovacao(8) == 0

def test_pontos_para_aprovacao_limite_sup():
    assert pontos_para_aprovacao(7.1) == 0

def test_pontos_para_aprovacao_limite_inf():
    assert pontos_para_aprovacao(6) == 1

# ========= + calcular_media_tres_notas + =========

def test_calcular_media_tres_notas():
    assert calcular_media_tres_notas(6, 6, 6) == 6

def test_calcular_media_tres_notas_quebrado():
    assert calcular_media_tres_notas(6, 6, 8) == 6.666666666666667