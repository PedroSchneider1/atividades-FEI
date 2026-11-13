# Exercício 1 — Modalidade de Frete

> **Objetivo de estudo:** ver, na prática, que uma suíte com **poucos testes** deixa
> a **maioria dos mutantes vivos**, e que cada mutante vivo aponta uma **lacuna
> concreta** nos testes. Depois, ver como o *estilo do assert* muda o escore.

Todos os números abaixo foram obtidos rodando de verdade (`pytest 9.1.1`,
`pytest-cov 7.1.0`, `mutmut 3.8.0`, Python 3.12). Os logs brutos estão em `logs/`.

---

## O código sob teste (`src/frete.py`)

```python
def modalidade_frete(peso, distancia):
    if peso <= 0 or peso > 30:                  # linha 2  -> validação do peso
        raise ValueError("Peso invalido")       # linha 3
    if distancia < 0 or distancia > 5000:       # linha 4  -> validação da distância
        raise ValueError("Distancia invalida")  # linha 5
    if peso > 20:                               # linha 6
        return "Transportadora"                 # linha 7
    if distancia <= 10:                         # linha 8
        return "Motoboy"                        # linha 9
    elif distancia <= 500:                      # linha 10
        return "Correio expresso"               # linha 11
    else:
        return "Correio economico"              # linha 13
```

**Regras que o código implementa** (as "fronteiras" são o que os mutantes atacam):

| Faixa | Resultado |
|---|---|
| `peso <= 0` ou `peso > 30` | erro "Peso invalido" |
| `distancia < 0` ou `distancia > 5000` | erro "Distancia invalida" |
| `peso > 20` | Transportadora |
| `distancia <= 10` | Motoboy |
| `distancia <= 500` | Correio expresso |
| acima disso | Correio economico |

---

## (a) Cobertura de ramos e mutmut na suíte inicial

**Suíte inicial** (`etapas/a_inicial/test_frete.py`): 2 testes —
`modalidade_frete(5, 300)` e `modalidade_frete(2, 1000)`.

| Medida | Resultado |
|---|---|
| **Cobertura de ramos** | **64 %** (12 comandos, 4 não executados; 10 ramos, 4 parciais) |
| Linhas que **nunca** rodam | **3, 5, 7, 9** |
| Mutantes **gerados** | **36** |
| Mutantes **mortos** | **6** |
| Mutantes **vivos** | **30** |
| **Escore de mutação** | 6 / 36 = **16,7 %** |

> **Como ler "Missing 3, 5, 7, 9":** são exatamente os `raise` de peso e de
> distância, o `return "Transportadora"` e o `return "Motoboy"`. Nenhum dos dois
> testes chega a eles (5 kg/300 km vai para "expresso"; 2 kg/1000 km vai para
> "econômico").

---

## (b) Agrupando os 30 vivos pelo trecho de código

Use `mutmut show NOME` para ver a mudança. Os 30 vivos se agrupam assim:

| Linha | Trecho original | Mutantes vivos (mutmut_N) | O que mudou | Linha executada pela suíte? |
|---|---|---|---|---|
| 2 | `peso <= 0 or peso > 30` | 1, 2, 3, 4, 5 | `or→and`; `<=→<`; `0→1`; `>→>=`; `30→31` | ✅ sim |
| **3** | `raise ValueError("Peso invalido")` | **6, 7, 8, 9** | `None`; `"XX…XX"`; minúscula; MAIÚSCULA | ❌ **NÃO** |
| 4 | `distancia < 0 or distancia > 5000` | 10, 11, 12, 13, 14 | `or→and`; `<→<=`; `0→1`; `>→>=`; `5000→5001` | ✅ sim |
| **5** | `raise ValueError("Distancia invalida")` | **15, 16, 17, 18** | idem (mensagem) | ❌ **NÃO** |
| 6 | `peso > 20` | 19, 20 | `>→>=`; `20→21` | ✅ sim |
| **7** | `return "Transportadora"` | **21, 22, 23** | texto alterado | ❌ **NÃO** |
| 8 | `distancia <= 10` | 24, 25 | `<=→<`; `10→11` | ✅ sim |
| **9** | `return "Motoboy"` | **26, 27, 28** | texto alterado | ❌ **NÃO** |
| 10 | `distancia <= 500` | 29, 30 | `<=→<`; `500→501` | ✅ sim |

**Resumo:** 14 vivos estão em linhas que a suíte **não executa** (3, 5, 7, 9) e
16 estão em linhas **executadas**, mas com **fronteiras** que ninguém testou.

> 💡 **Duas causas diferentes para sobreviver:**
> 1. **Linha não executada** → o mutante nem é *alcançado* (falha o "Reach").
>    Qualquer mutante ali sobrevive, por definição.
> 2. **Linha executada, mas valor errado** → o mutante é alcançado, porém a
>    entrada usada (5/300, 2/1000) está **longe das fronteiras** (0, 10, 20, 30,
>    500, 5000), então o resultado é o mesmo do original.

Os 6 mortos (31 a 36) são só as strings de `"Correio expresso"` e
`"Correio economico"`, as únicas linhas de retorno que os testes confirmam.

---

## (c) Testes novos até matar todos

Arquivo final: `etapas/c_final/test_frete.py` (também em `tests/`) — **20 testes**
(2 originais + 18 novos, contando as parametrizações).

**Estratégia:** para cada comparação do código, testar **os dois lados da
fronteira** (análise de valor-limite) e conferir a **mensagem exata** das exceções.

| Teste novo | Entrada | Mata |
|---|---|---|
| `peso_invalido…mensagem_exata` (0, −1, 30.01, 31) | peso inválido, dist. 100 | 1, 2, 5 **e** todos de mensagem de peso (6–9) |
| `peso_minimo_valido` | `(1, 5)` → Motoboy | 3 (`<= 1`) |
| `peso_maximo_valido_30` | `(30, 5)` → Transportadora | 4 (`>= 30`) |
| `distancia_invalida…mensagem_exata` (−1, 5001) | dist. inválida | 10, 14 **e** mensagens de distância (15–18) |
| `distancia_zero_valida` | `(5, 0)` → Motoboy | 11 (`<= 0`), 12 (`< 1`) |
| `distancia_5000_valida` | `(5, 5000)` → econômico | 13 (`>= 5000`) |
| `peso_20_nao_e_transportadora` | `(20, 300)` → expresso | 19 (`>= 20`) |
| `peso_21_e_transportadora` | `(21, 5)` → Transportadora | 20 (`> 21`) |
| `transportadora_texto_exato` | `(25, 300)` | 21, 22, 23 |
| `distancia_10_e_motoboy` | `(5, 10)` | 24 (`< 10`) |
| `distancia_11_e_correio_expresso` | `(5, 11)` | 25 (`<= 11`) |
| `motoboy_texto_exato` | `(5, 3)` | 26, 27, 28 |
| `distancia_500_e_correio_expresso` | `(5, 500)` | 29 (`< 500`) |
| `distancia_501_e_correio_economico` | `(5, 501)` | 30 (`<= 501`) |

**Resultado final**

| Medida | Antes (a) | Depois (c) |
|---|---|---|
| Cobertura de ramos | 64 % | **100 %** |
| Gerados | 36 | 36 |
| Mortos | 6 | **36** |
| Vivos | 30 | **0** |
| Equivalentes | — | **0** |
| **MS** | 16,7 % | **36 / 36 = 100 %** |

**Existe algum equivalente?** Não. Para cada mutante há uma entrada em que o
comportamento muda. Exemplo: `peso <= 0` → `peso <= 1` — com `peso = 1` o original
aceita e o mutante lança erro; é **observável**, logo **não** equivalente.

---

## (d) `str(erro.value) == msg` × `pytest.raises(..., match=msg)`

Arquivo: `etapas/d_match/test_frete.py` (trocando apenas o estilo do assert).

```python
# versão (c)  — exata
with pytest.raises(ValueError) as erro:
    modalidade_frete(peso, 100)
assert str(erro.value) == "Peso invalido"

# versão (d)  — match
with pytest.raises(ValueError, match="Peso invalido"):
    modalidade_frete(peso, 100)
```

| | (c) `==` | (d) `match=` |
|---|---|---|
| Gerados | 36 | 36 |
| Mortos | 36 | **34** |
| Vivos | 0 | **2** (`mutmut_7` e `mutmut_16`) |
| **MS** | **100 %** | **34 / 36 = 94,4 %** |

**Por que o MS caiu?** O `match=` usa **`re.search`**: procura o padrão como
*trecho* **em qualquer posição** da mensagem. Os dois sobreviventes são:

```python
raise ValueError("XXPeso invalidoXX")        # mutmut_7
raise ValueError("XXDistancia invalidaXX")   # mutmut_16
```

`"Peso invalido"` **está contido** em `"XXPeso invalidoXX"`, então o `match` passa
e o mutante **não é revelado**. Os outros mutantes de texto morrem porque:

- `ValueError(None)` → a mensagem vira `"None"` → não casa;
- `"peso invalido"` / `"PESO INVALIDO"` → o regex diferencia maiúsculas de minúsculas → não casa.

**Moral da história:** `match=` verifica *"a mensagem contém isto"*, enquanto `==`
verifica *"a mensagem é exatamente isto"*. O segundo é mais rigoroso.

**Bônus verificado:** ancorar o regex recupera os 100 % (`etapas/e_match_ancorado/`):

```python
with pytest.raises(ValueError, match="^Peso invalido$"):   # ^ início, $ fim
```

Resultado: 36 mortos / 36 → **100 %**.

---

## ✅ O que levar deste exercício

1. **Cobertura 64 % já denuncia linhas não testadas**, mas só o mutmut mostra *quantas
   fronteiras* estão soltas mesmo nas linhas cobertas.
2. **Toda comparação (`<`, `<=`, `>`, `>=`) pede dois testes**: um de cada lado da fronteira.
3. **Mensagens de erro também são comportamento**: se você não confere o texto, `"XX…XX"` passa.
4. **O estilo do assert muda o escore** (`==` > `match=` sem âncora).
