# Exercício 2 — Cashback

> **Objetivo de estudo:** entender por que **100 % de cobertura de ramos** pode
> conviver com **23 % de escore de mutação**, e usar o modelo **RIPR**
> (*Reach, Infect, Propagate, Reveal* = Alcançar, Infectar, Propagar, Revelar)
> para explicar cada mutante que sobrevive.

Números obtidos rodando de verdade (`mutmut 3.8.0`). Logs em `logs/`.

---

## O código sob teste (`src/cashback.py`)

Especificação: cada compra de **R$ 100 ou mais** devolve **5 %** do valor; o total
devolvido é arredondado a **duas casas**.

```python
def cashback(compras):
    total = 0
    for valor in compras:
        if valor >= 100:
            total += valor * 0.05
    return round(total, 2)
```

---

## (a) Cobertura de ramos × escore de mutação

**Suíte inicial** (um único teste):

```python
assert cashback([50, 100, 200]) > 0
```

| Medida | Resultado |
|---|---|
| **Cobertura de ramos** | **100 %** (6 comandos, 4 ramos, nada faltando) |
| Mutantes gerados | **13** |
| Mortos | **3** (`mutmut_1`, `6`, `9`) |
| Vivos | **10** |
| **Escore de mutação** | 3 / 13 = **23,1 %** |

### Por que os dois números são tão diferentes?

- **Cobertura mede execução:** "a linha/ramo foi percorrida por algum teste?".
  A lista `[50, 100, 200]` passa pelo `if` verdadeiro (100, 200) e falso (50), pelo
  `+=`, pelo `return`. Logo, 100 %.
- **Mutação mede verificação:** "se eu **estragar** o código, algum `assert`
  **reclama**?". O `assert … > 0` só reclama se o resultado deixar de ser positivo.
  Existem **infinitos** resultados errados que ainda são positivos.

> 🧠 **Analogia:** cobertura é conferir que o aluno *escreveu algo* em todas as
> questões da prova. Mutação é conferir que o que ele escreveu está *certo*.

**Os 3 mortos** só morreram porque quebraram de um jeito "grosseiro":

| Mutante | Mudança | Por que morreu |
|---|---|---|
| 1 | `total = None` | `None += …` dá `TypeError` (o teste explode) |
| 6 | `total -= valor * 0.05` | resultado **negativo** (−15), e `-15 > 0` é falso |
| 9 | `round(None, 2)` | `TypeError` |

**Os 10 vivos** (todos ainda dão resultado positivo): `total = 1`, `> 100`, `>= 101`,
`total = valor*0.05` (em vez de `+=`), `/ 0.05`, `* 1.05`, `round(total, None)`,
`round(2)`, `round(total, )` e `round(total, 3)`.

---

## (b) Trocando `> 0` pelo valor exato

Cálculo: `50` não entra; `100 × 0,05 = 5,0`; `200 × 0,05 = 10,0` → **15,0**.

```python
assert cashback([50, 100, 200]) == 15.0     # etapas/b_exato/test_cashback.py
```

| Medida | Antes (`> 0`) | Depois (`== 15.0`) |
|---|---|---|
| Mortos | 3 | **10** |
| Vivos | 10 | **3** |
| MS | 23,1 % | **10 / 13 = 76,9 %** |

**Continuam vivos: 3 mutantes — `mutmut_10`, `mutmut_12` e `mutmut_13`**, todos na
linha `return round(total, 2)`.

```python
round(total, None)   # mutmut_10  → round(15.0, None) devolve 15  (int)
round(total, )       # mutmut_12  → round(15.0)       devolve 15  (int)
round(total, 3)      # mutmut_13  → round(15.0, 3)    devolve 15.0
```

> Só trocar o `assert` já matou **7** mutantes (de 23 % para 77 %). Isso mostra que
> o problema principal era o **assert fraco** (a *revelação*).

---

## (c) Qual condição RIPR **não** foi atendida nos 3 vivos?

Lembrete das 4 condições para um teste **matar** um mutante:

1. **Alcançar (Reach):** a linha mutada é executada?
2. **Infectar (Infect):** o **estado interno** fica diferente do original?
3. **Propagar (Propagate):** a diferença chega até a **saída** da função?
4. **Revelar (Reveal):** o `assert` **percebe** a diferença?

| Mutante | Alcançar | Infectar | Propagar | Revelar | Condição que falhou |
|---|:-:|:-:|:-:|:-:|---|
| **10** `round(total, None)` | ✅ | ⚠️ só no *tipo* (`15` int × `15.0` float) | ✅ | ❌ | **Revelar** (e infecção apenas superficial) |
| **12** `round(total, )` | ✅ | ⚠️ só no *tipo* | ✅ | ❌ | **Revelar** (e infecção apenas superficial) |
| **13** `round(total, 3)` | ✅ | ❌ `15.0` arredondado a 3 casas **é** `15.0` | — | ❌ | **Infectar** |

**Explicando com calma:**

- **Mutante 13:** como o total já é `15.0` (nenhuma casa decimal além da primeira),
  arredondar a 2 ou a 3 casas dá **o mesmo número**. O estado **não é infectado**:
  nada de diferente acontece. Falha a **infecção**.
- **Mutantes 10 e 12:** `round(15.0)` devolve `15` (um `int`). O valor *é* diferente
  na representação (`int` × `float`), mas em Python `15 == 15.0` é **verdadeiro**. O
  efeito sai da função (propaga), porém o `assert ==` **não percebe**. Falha a
  **revelação**. Como o número em si não mudou, também é uma infecção fraca.

> Em ambos os casos, o *problema real* é a **entrada**: `15.0` não "exercita" o
> arredondamento. Um total com **mais de 2 casas decimais** exercitaria.

---

## (d) Testes novos até MS = 100 %

Arquivo: `etapas/d_final/test_cashback.py` — **5 testes**.

```python
def test_cashback_exige_arredondamento_em_duas_casas():
    # 111.11 * 0.05 = 5.5555
    assert cashback([111.11]) == 5.56
```

Por que **111,11** mata os três:

| Versão | `round(5.5555, …)` | Resultado do teste |
|---|---|---|
| original `round(t, 2)` | **5.56** | ✅ passa |
| `mutmut_13` `round(t, 3)` | 5.556 | ❌ falha → **morto** |
| `mutmut_10` `round(t, None)` | 6 | ❌ falha → **morto** |
| `mutmut_12` `round(t, )` | 6 | ❌ falha → **morto** |

(Os outros 3 testes novos — `[100]`, `[99.99]`, `[]` — documentam fronteiras e a
lista vazia; não eram necessários para o escore, mas tornam a suíte mais legível.)

| Medida | Resultado final |
|---|---|
| Cobertura de ramos | 100 % |
| Mortos / gerados | **13 / 13** |
| **MS** | **100 %** |

### Que característica a nova entrada precisou ter?

> **O cashback calculado precisa ter mais de duas casas decimais** (um valor
> "quebrado", como 5,5555), para que o `round(…, 2)` **realmente altere o
> número**. Com `15.0` o arredondamento era invisível.

Em termos RIPR: a nova **entrada** resolve **alcançar/infectar**; o `assert` exato
(item b) resolve **revelar**. As duas coisas juntas são necessárias.

---

## ✅ O que levar deste exercício

1. **Cobertura de 100 % ≠ testes bons.** Aqui: 100 % de ramos com 23 % de mutantes mortos.
2. **`assert x > 0` é quase um "não quebrou".** Prefira o **valor exato esperado**.
3. **Assert exato resolve a *revelação*; entradas novas resolvem *alcançar* e *infectar*.**
4. Ao escolher dados de teste, pergunte: *"esta entrada faz cada operação (inclusive o
   `round`) produzir algo diferente do que produziria com o código errado?"*
