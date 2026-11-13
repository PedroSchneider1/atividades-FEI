# Exercício 3 — Cotações da Semana

> **Objetivo de estudo:** aprender a **classificar mutantes vivos** em
> *equivalentes* (não dá para matar, pois o programa se comporta igual) e *não
> equivalentes* (dá para matar com um teste melhor), e ver como o **escore de
> mutação** exclui os equivalentes.

Números obtidos rodando de verdade (`mutmut 3.8.0`). Logs em `logs/`.

---

## O código sob teste (`src/cotacoes.py`)

```python
def menor_preco(precos):                      # devolve o MENOR PREÇO (um valor)
    if not precos:
        raise ValueError("sem cotacoes")
    m = precos[0]
    for p in precos[1:]:
        if p < m:
            m = p
    return m


def dia_da_compra(precos):                    # devolve a POSIÇÃO do ÚLTIMO dia de menor preço
    if not precos:
        raise ValueError("sem cotacoes")
    pos = 0
    for i in range(1, len(precos)):
        if precos[i] <= precos[pos]:
            pos = i
    return pos
```

> 🔑 **Repare na diferença de retorno:** `menor_preco` devolve um **valor**;
> `dia_da_compra` devolve uma **posição**. Esse detalhe é a chave do item (d).

---

## (a) Suíte inicial e mutmut

`etapas/a_inicial/test_cotacoes.py` — **8 testes**: as listas `[32, 28, 35, 25, 30]`
(mín. 25 na posição 3), `[40]` e `[20, 27]` para as duas funções (valor exato) e a
lista vazia com `pytest.raises(ValueError)` **sem** conferir a mensagem.

| Medida | Resultado |
|---|---|
| Cobertura de ramos | **100 %** |
| Mutantes gerados | **22** (9 em `menor_preco` + 13 em `dia_da_compra`) |
| Mortos | **11** |
| Vivos | **11** |

Mudança de cada vivo (`mutmut show NOME`):

| Mutante vivo | Função | Mudança |
|---|---|---|
| `x_menor_preco__mutmut_2` | menor_preco | `ValueError("sem cotacoes")` → `ValueError(None)` |
| `x_menor_preco__mutmut_3` | menor_preco | mensagem → `"XXsem cotacoesXX"` |
| `x_menor_preco__mutmut_4` | menor_preco | mensagem → `"SEM COTACOES"` |
| `x_menor_preco__mutmut_7` | menor_preco | `precos[1:]` → `precos[2:]` |
| `x_menor_preco__mutmut_8` | menor_preco | `if p < m` → `if p <= m` |
| `x_dia_da_compra__mutmut_2` | dia_da_compra | `ValueError(None)` |
| `x_dia_da_compra__mutmut_3` | dia_da_compra | mensagem → `"XXsem cotacoesXX"` |
| `x_dia_da_compra__mutmut_4` | dia_da_compra | mensagem → `"SEM COTACOES"` |
| `x_dia_da_compra__mutmut_9` | dia_da_compra | `range(1, len(precos))` → `range(len(precos))` |
| `x_dia_da_compra__mutmut_11` | dia_da_compra | `range(1, len(precos))` → `range(2, len(precos))` |
| `x_dia_da_compra__mutmut_12` | dia_da_compra | `precos[i] <= precos[pos]` → `precos[i] < precos[pos]` |

---

## (b) Classificação: equivalente × não equivalente

**Definição prática:** um mutante é **equivalente** se **nenhuma entrada** faz o
programa mutante se comportar de forma diferente do original. Basta **uma** entrada
que diferencie para ele ser **não equivalente** (matável).

| Mutante | Classe | Justificativa |
|---|---|---|
| menor_preco **2, 3, 4** (mensagem) | ❌ **Não equiv.** | Para `[]` o original lança `"sem cotacoes"`; o mutante lança `None`/`XX…XX`/`SEM COTACOES`. A mensagem é o que o chamador recebe, ou seja, **comportamento observável**. A suíte sobrevive só porque **não confere** o texto. |
| menor_preco **7** (`[1:]`→`[2:]`) | ❌ **Não equiv.** | `[30, 20, 25]`: original = **20**; mutante pula o 2º elemento e devolve **25**. Sobrevive porque nos testes o mínimo nunca está na posição 1. |
| menor_preco **8** (`<` → `<=`) | ✅ **EQUIVALENTE** | Só muda quando `p == m`. Nesse caso `m = p` atribui um valor **igual ao que `m` já tem**. Como a função devolve o **valor** (não a posição), o resultado é sempre o mesmo. |
| dia_da_compra **2, 3, 4** (mensagem) | ❌ **Não equiv.** | Mesma justificativa das mensagens acima. |
| dia_da_compra **9** (`range(1,n)`→`range(n)`) | ✅ **EQUIVALENTE** | A única iteração extra é `i = 0`: compara `precos[0] <= precos[0]` (sempre verdadeiro) e faz `pos = 0` — que **já era** o valor de `pos`. Nada muda. |
| dia_da_compra **11** (`range(1,n)`→`range(2,n)`) | ❌ **Não equiv.** | `[30, 20, 25]`: original = **1**; mutante nunca olha o índice 1 e devolve outra coisa. |
| dia_da_compra **12** (`<=` → `<`) | ❌ **Não equiv.** | A especificação pede o **ÚLTIMO** dia de menor preço. `[20, 30, 20]`: original = **2**; mutante = **0** (fica no primeiro). |

**Resumo:** 2 equivalentes (8 e 9) + 9 não equivalentes (2, 3, 4, 7 | 2, 3, 4, 11, 12).

**Evidência por força bruta** (`extras/equivalencia_forca_bruta.py`, saída em
`logs/extras_equivalencia_forca_bruta.txt`): comparei original × mutante em
**5 460 listas** (tamanho 1 a 6, valores 0 a 3).

| Mutante | Resultado |
|---|---|
| menor_preco 8 | nenhuma diferença → equivalente |
| dia_da_compra 9 | nenhuma diferença → equivalente |
| menor_preco 7 | contra-exemplo: `[1, 0]` → original 0, mutante 1 |
| dia_da_compra 11 | contra-exemplo: `[0, 0]` → original 1, mutante 0 |
| dia_da_compra 12 | contra-exemplo: `[0, 0]` → original 1, mutante 0 |

> ⚠️ Força bruta **não é prova** (só testa um espaço finito). Ela dá confiança; a
> prova é o argumento lógico da tabela acima.

**Ressalvas honestas:**

- *Mensagens:* a especificação do enunciado diz apenas que a função "devolve o menor
  preço". Se o seu professor considerar o texto da mensagem **fora** da especificação,
  poderia tratá-los como "equivalentes em relação à especificação". Eu os trato como
  **não equivalentes** porque o texto é comportamento **observável** pelo chamador —
  e é o critério estrito de equivalência.
- *Mutante 8:* se os preços fossem objetos distinguíveis apesar de iguais (ex.: `1`
  e `1.0`, ou `Decimal('1.0')` × `Decimal('1.00')`), a ordem de escolha apareceria. Para
  preços numéricos, "iguais" são indistinguíveis, e a especificação não exige mais.

---

## (c) Testes que matam os não equivalentes + MS antes/depois

Arquivo final: `etapas/c_final/test_cotacoes.py` — **14 testes** (8 originais + 6 novos).

| Teste novo | Entrada → esperado | Mata |
|---|---|---|
| `menor_preco_lista_vazia_mensagem_exata` | `[]` → `str(erro.value) == "sem cotacoes"` | menor_preco 2, 3, 4 |
| `menor_preco_minimo_na_segunda_posicao` | `[30, 20, 25]` → `20` | menor_preco 7 |
| `dia_da_compra_lista_vazia_mensagem_exata` | `[]` → `"sem cotacoes"` | dia_da_compra 2, 3, 4 |
| `dia_da_compra_minimo_na_segunda_posicao` | `[30, 20, 25]` → `1` | dia_da_compra 11 |
| `dia_da_compra_empate_devolve_o_ultimo_dia` | `[20, 30, 20]` → `2` | dia_da_compra 12 |
| `dia_da_compra_empate_consecutivo` | `[25, 25]` → `1` | dia_da_compra 12 (reforço) |

Fórmula do laboratório: **MS = mortos / (gerados − equivalentes)**

| Momento | Mortos | Gerados | Equivalentes | **MS** |
|---|---|---|---|---|
| **Antes** (suíte inicial) | 11 | 22 | 2 | 11 / 20 = **55 %** |
| **Depois** (suíte final) | 20 | 22 | 2 | 20 / 20 = **100 %** |

(Sem descontar os equivalentes, o escore "bruto" iria de 50 % para 90,9 % — e os 2
vivos que sobram são exatamente `menor_preco_8` e `dia_da_compra_9`.)

---

## (d) Por que a *mesma* troca gera equivalente num lugar e não no outro?

A mutação é a mesma ideia (`<` ↔ `<=`), mas o **resultado** é diferente porque
as funções **devolvem coisas diferentes**:

| | `menor_preco` (`<` → `<=`) | `dia_da_compra` (`<=` → `<`) |
|---|---|---|
| O que devolve | o **valor** do menor preço | a **posição** do menor preço |
| O que muda quando há **empate** (`p == m`)? | Troca `m` por um valor **igual** a ele → `m` continua com o mesmo valor | Troca `pos` por **outra posição** (a do empate) → `pos` fica **diferente** |
| Resultado observável | **idêntico** em toda entrada | **diferente**: `[20, 30, 20]` → 2 (orig.) × 0 (mutante) |
| Classe | ✅ **Equivalente** | ❌ **Não equivalente** |

> **Frase para memorizar:** *equivalência depende do que a função **devolve** e do que
> a **especificação exige**.* Em `dia_da_compra`, a especificação diz **"último"** dia —
> então desempatar para a direita **é** o requisito. Em `menor_preco`, ninguém
> consegue distinguir "o primeiro 20" de "o último 20": ambos valem 20.

Intuição: pense em dois funcionários empatados em vendas.
- *"Qual foi a maior venda?"* → resposta é o **valor**; empatados, tanto faz quem você citou.
- *"Quem foi o último a bater a meta?"* → resposta é a **pessoa**; trocar o critério de desempate muda a resposta.

---

## ✅ O que levar deste exercício

1. **Todo vivo precisa de um veredito:** equivalente (justifique) ou não equivalente (escreva o teste).
2. **Para ser não equivalente, basta UM contra-exemplo** — procure entradas nas **fronteiras** e nos **empates**.
3. **Equivalentes ficam de fora do denominador** do MS.
4. **Mensagens de exceção, posições (`[1:]`) e empates** são lugares clássicos onde suítes iniciais falham.
