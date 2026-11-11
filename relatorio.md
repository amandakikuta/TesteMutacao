# RELATÓRIO

## Informações
* **Linguagem:** Python
* **Programa utilizado:** Gerado por IA
* **Ferramenta utilizada:** Cosmic Ray
* **Quantidade de casos de teste:** 20

## Mutantes

* **Mutantes gerados:** 112
* **Mutantes mortos:** 110
* **Mutantes equivalentes:** 2
* **Score:** 1.0

## Principais arquivos e pastas

* **./codigo/program.py**: Programa original
* **./tests/test_program.py**: Arquivo com os casos de teste
* **./todos_mutantes/**: Mutantes gerados sobre o programa original

## Mutantes Equivalentes

```
 def maior_nota(nota1, nota2):
-    if nota1 > nota2:
+    if nota1 >= nota2:
         return nota1
     return nota2
```

```
 def pontos_para_aprovacao(media):
-    if media >= 7:
+    if media > 7:
         return 0
     return 7 - media
```

## Como executar

### 1. Inicializar ambiente virtual

```
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar Cosmic Ray

```
python -m pip install pytest cosmic-ray
```

### 3. Executar os testes com pytest

```
python -m pytest -v
```

### 4. Inicializar a sessão

```
cosmic-ray init cosmic-ray.toml <session_name>.sqlite
```

### 5. Executar os mutantes

```
cosmic-ray exec cosmic-ray.toml <session_name>.sqlite
```

### 6. Gerar relatório

```
cr-report session.sqlite
```

Para mostrar apenas os mutantes que sobreviveram utilize **_--surviving-only_**

Para mostrar a diferença entre o programa original e o mutante utilize **_--show-diff_**