# Exercício 4 — Multa por Atraso

> **Objetivo de estudo:** (1) ver que a **análise de valor-limite** (aula 6) já mata
> a maior parte dos mutantes, e que a **mutação mostra o que ficou de fora**;
> (2) conhecer **mutantes de segunda ordem** e o **efeito de acoplamento**
> (Offutt, 1992).

Números obtidos rodando de verdade (`mutmut 3.8.0`). Logs em `logs/`.

---

## O código sob teste (`src/multa.py`)

Regras: fora de **0 a 60** dias → `ValueError`; até **5** dias → sem multa; depois,
**1 % por dia além do quinto**; valor final arredondado a 2 casas.

```python
def valor_com_multa(valor, dias):
    if dias < 0 or dias > 60:
        raise ValueError("atraso invalido")
    if dias <= 5:
        multa = 0
    else:
        multa = 0.01 * (dias - 5)
    total = valor * (1 + multa)
    return round(total, 2)
```

---

## (a) Suíte por análise de valor-limite (escrita **sem** rodar ferramenta)

Raciocínio (só lendo a especificação):

```
dias:     ... -1 | 0 .. 5 | 6 .. 60 | 61 ...
            inválido  sem multa  com multa  inválido
valores-limite:  -1, 0, 1 | 4, 5, 6 | 59, 60, 61    (+ nominal 30)
```

Usei `valor = 100` para as contas ficarem simples (cada dia de multa = R$ 1,00).

| Teste | `dias` | Esperado |
|---|---|---|
| `dias_invalidos_lancam_erro` | −1, 61 | `ValueError` |
| `ate_cinco_dias_sem_multa` | 0, 1, 4, 5 | 100.0 |
| `seis_dias_um_por_cento` | 6 | 101.0 |
| `trinta_dias_nominal` | 30 | 125.0 |
| `cinquenta_e_nove_dias` | 59 | 154.0 |
| `sessenta_dias_maximo_valido` | 60 | 155.0 |

Arquivo: `etapas/a_bva/test_multa.py` — **10 testes** (contando parametrizações).

---

## (b) Cobertura de ramos e MS da suíte BVA

| Medida | Resultado |
|---|---|
| Cobertura de ramos | **100 %** |
| Mutantes gerados | **26** |
| Mortos | **19** |
| Vivos | **7** (`mutmut_6, 7, 8, 9, 23, 25, 26`) |
| **MS (bruto)** | 19 / 26 = **73,1 %** |

> A BVA, sem nenhuma ferramenta, já matou **19 dos 26** (todos os de comparações,
> `or→and`, constantes e operadores aritméticos). A mutação mostra o que **faltou**.

---

## (c) Cada vivo: teste que o mata **ou** justificativa de equivalência

| Vivo | Mudança | Veredito | O que o mata |
|---|---|---|---|
| 6 | `ValueError(None)` | ❌ não equiv. | `str(erro.value) == "atraso invalido"` |
| 7 | `ValueError("XXatraso invalidoXX")` | ❌ não equiv. | idem |
| 8 | `ValueError("ATRASO INVALIDO")` | ❌ não equiv. | idem |
| 23 | `round(total, None)` | ❌ não equiv. | `valor_com_multa(123.45, 7) == 125.92` |
| 25 | `round(total, )` | ❌ não equiv. | idem |
| 26 | `round(total, 3)` | ❌ não equiv. | idem |
| **9** | **`dias <= 5` → `dias < 5`** | ✅ **EQUIVALENTE** | — (justificativa abaixo) |

**Por que 6, 7, 8:** a BVA original usava `pytest.raises(ValueError)` **sem** conferir
a mensagem — o mesmo vício do exercício 1.

**Por que 23, 25, 26:** com `valor = 100` o resultado é `101.0`, `125.0`…, sempre com
poucas casas; o `round` nunca "infecta" nada. Precisa de entrada com **mais de 2
casas decimais**: `123,45 × 1,02 = 125,91900000000001` →

| Versão | Resultado |
|---|---|
| original `round(t, 2)` | **125.92** |
| `round(t, 3)` | 125.919 ❌ |
| `round(t)` / `round(t, None)` | 126 ❌ |

**Justificativa do equivalente (mutante 9):** a única entrada em que `dias <= 5` e
`dias < 5` se comportam diferente é `dias == 5`.

```
original  (dias <= 5): vai ao ramo `if`   →  multa = 0
mutante   (dias <  5): vai ao ramo `else` →  multa = 0.01 * (5 - 5) = 0.0
```

`multa` vale **zero** nos dois casos, então `total = valor * (1 + 0)` é **o mesmo
número**. A "fronteira" foi movida para um ponto onde a fórmula do `else` já dá
zero — mutante inofensivo.

**Ressalvas honestas** (verificadas em Python): com `valor` inteiro, o original
devolve `100` (int) e o mutante `100.0` (float) em `dias == 5`; os dois são `==`.
Com `Decimal`, o mutante falharia com `TypeError` onde o original funcionaria — mas o
original **também** quebra com `Decimal` a partir de 6 dias (`0.01` é float), então
`Decimal` não está no contrato da função. Para `int`/`float` (o que a especificação
espera) não há diferença de **valor**. 7 valores × 61 dias testados: nenhuma diferença.

**Suíte final:** `etapas/c_final/test_multa.py` — **13 testes**.

| Medida | (b) BVA | (c) Final |
|---|---|---|
| Cobertura de ramos | 100 % | 100 % |
| Mortos | 19 | **25** |
| Vivos | 7 | **1** (o equivalente) |
| Equivalentes | — | 1 |
| **MS = mortos / (gerados − equiv.)** | 19 / 25 = 76 % | **25 / 25 = 100 %** |

---

## (d) Dois mutantes de 1ª ordem juntos → mutante de **2ª ordem**

**Conceitos:**

- **1ª ordem:** uma única mudança no código (é o que o mutmut gera).
- **2ª ordem:** **duas** mudanças combinadas no mesmo programa.

**Escolhi dois mutantes que a suíte BVA mata:**

| | Mudança | Teste da BVA que o mata sozinho |
|---|---|---|
| `mutmut_10` | `if dias <= 5` → `if dias <= 6` | `dias = 6` (esperava 101.0) |
| `mutmut_17` | `0.01 * (dias - 5)` → `0.01 * (dias - 6)` | `dias = 30` etc. |

Aplicadas juntas, à mão (`extras/mutante_2a_ordem/multa.py`):

```python
def valor_com_multa(valor, dias):
    if dias < 0 or dias > 60:
        raise ValueError("atraso invalido")
    if dias <= 6:                      # <-- mudança 1 (era 5)
        multa = 0
    else:
        multa = 0.01 * (dias - 6)      # <-- mudança 2 (era 5)
    total = valor * (1 + multa)
    return round(total, 2)
```

---

## (e) A suíte mata o mutante de 2ª ordem?

**Sim.** Saída real (`logs/extras_mutante_2a_ordem_manual.txt`):

```
suite a_bva:    4 failed, 6 passed
   test_seis_dias_um_por_cento           assert 100 == 101.0
   test_trinta_dias_nominal              assert 124.0 == 125.0
   test_cinquenta_e_nove_dias            assert 153.0 == 154.0
   test_sessenta_dias_maximo_valido      assert 154.0 == 155.0

suite c_final:  5 failed, 8 passed
```

### Relação com o **efeito de acoplamento** e com **Offutt (1992)**

- **Hipótese do programador competente:** os defeitos reais são, em geral, **pequenos**
  (um `<` no lugar de `<=`, um `+1` esquecido). Por isso mutantes de 1ª ordem
  representam bem os erros reais.
- **Efeito de acoplamento** (DeMillo, Lipton e Sayward, 1978): *defeitos complexos são
  "acoplados" a defeitos simples* — um conjunto de testes capaz de distinguir **todos
  os defeitos simples** tende a distinguir também os **complexos**.
- **Offutt (1992)** investigou isso **empiricamente**: conjuntos de teste que matavam
  os mutantes de 1ª ordem também mataram a quase totalidade (≈ 99 %, segundo o artigo
  — vale conferir o número exato na fonte) dos de 2ª ordem.
- **Consequência prática:** basta gerar mutantes **simples** (baratos: poucos) em vez
  de todas as combinações (explosão combinatória), pois os complexos "vêm de graça".

**Neste exercício** o mutante escolhido morreu por **vários** testes ao mesmo tempo
(4 na BVA) — é o acoplamento em ação: cada mudança isolada já era detectada, e a
combinação continuou sendo.

### 🔬 Experimento extra: **todos** os pares, não só um

Um único exemplo não prova nada, então rodei `extras/segunda_ordem_experimento.py`,
que combina **todos os pares** de mutantes de 1ª ordem **já mortos** (em linhas
diferentes) e roda a suíte contra cada um:

| Suíte | Mortos na 1ª ordem | Pares (2ª ordem) testados | Mortos | **Sobreviventes** |
|---|---|---|---|---|
| BVA (`a_bva`) | 19 | 143 | 143 | **0** |
| Final (`c_final`) | 25 | 260 | 260 | **0** |

Nenhum mutante de 2ª ordem sobreviveu: **o efeito de acoplamento se confirmou**
neste programa.

> ⚠️ **Limitações:** é um programa **pequeno**; só combinei mutantes em linhas
> diferentes; e, em teoria, duas falhas poderiam se **mascarar** (uma cancelar a
> outra). Isso é raro, e é exatamente o que o artigo de Offutt quantifica.

---

## ✅ O que levar deste exercício

1. **BVA sozinha já mata ~73 % dos mutantes** (19/26) — é uma técnica forte e barata.
2. **A mutação revela o que a BVA não cobre:** o **texto das mensagens** e a **precisão
   numérica** (`round`) — a BVA olha as *fronteiras das entradas*, não a *qualidade do oráculo*.
3. **Mutante equivalente em fronteira:** mover `<=` para `<` pode ser inofensivo se o
   outro ramo já produz o mesmo resultado na fronteira (`multa = 0.01 * 0`).
4. **Acoplamento:** testar bem os defeitos simples protege contra os compostos.
