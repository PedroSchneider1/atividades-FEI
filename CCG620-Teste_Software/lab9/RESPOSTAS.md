Convenções: **MS = mortos / (gerados − equivalentes)**. Ícones do mutmut: 🎉 morto, 🙁 vivo.

Estrutura entregue (mesmos nomes do PDF):

```
lab09/
├── .gitignore                       (mutants/)
├── ex1/  pyproject.toml  src/classificacao.py   tests/test_classificacao.py   variante_d/test_classificacao_match.py
├── ex2/  pyproject.toml  src/carrinho.py        tests/test_carrinho.py
├── ex3/  pyproject.toml  src/temperaturas.py    tests/test_temperaturas.py
└── ex4/  pyproject.toml  src/parcelamento.py    tests/test_parcelamento.py   segunda_ordem/…
```

Resumo:

| Ex. | Suíte inicial: cobertura | MS inicial | MS final | Equivalentes |
|---|---|---|---|---|
| 1 | 64 % (ramos) | 6/36 = **16,7 %** | 36/36 = **100 %** | 0 |
| 2 | 100 % (ramos) | 4/16 = **25 %** (com assert exato: 13/16 = 81,25 %) | 16/16 = **100 %** | 0 |
| 3 | 100 % (ramos) | 11/(22−2) = **55 %** (bruto 11/22 = 50 %) | 20/(22−2) = **100 %** | 2 |
| 4 | 100 % (ramos) | 25/27 = **92,6 %** | 26/(27−1) = **100 %** | 1 |

---

## Exercício 1 — Situação do Aluno

### a) Cobertura e mutmut (suíte inicial, 2 testes)

- Cobertura de ramos: **64 %** (12 comandos, 4 não executados; 10 ramos, 4 parciais). Linhas não executadas: **3, 5, 7 e 11**.
- mutmut: **36 gerados, 6 mortos, 30 vivos** → MS = 6/36 = 16,7 %.
- Os 6 mortos são só as mutações de *string* de `"Aprovado"` (26–28) e `"Reprovado"` (34–36), as únicas linhas de retorno que a suíte exercita.

### b) Vivos agrupados pela causa

| Grupo | Causa | Mutantes | Qtd |
|---|---|---|---|
| A | **Linha que a suíte nem executa** (falha *alcançar*): `raise` da média (l. 3), `raise` da presença (l. 5), `return "Reprovado por falta"` (l. 7), `return "Recuperacao"` (l. 11). São mutações de mensagem (`None`, `XX…XX`, minúsculas, maiúsculas) | 6–9, 15–18, 21–23, 31–33 | **14** |
| B | Linhas 2 e 4 **são executadas**, mas nenhuma entrada inválida ou de fronteira (0, 10, 100) muda o resultado da condição (`or→and`, `<→<=`, `<0→<1`, `>10→>=10`, `>10→>11`, idem para presença) | 1–5, 10–14 | **10** |
| C | Linhas 6, 8 e 10 **são executadas**, mas sem valores na fronteira 75 / 7.0 / 5.0 (`<75→<=75`, `<76`, `>=7.0→>7.0`, `>=8.0`, `>=5.0→>5.0`, `>=6.0`) | 19, 20, 24, 25, 29, 30 | **6** |

Total: 14 + 10 + 6 = 30. Dos 30 vivos, **14 estão em linhas que a suíte nem executa**.

### c) Testes acrescentados e MS final

Ver `ex1/tests/test_classificacao.py` (19 testes, cobertura 100 %). Idéias-chave:

- média/presença inválidas **coladas** na fronteira (`-0.1`, `10.1`, `-1`, `101`) **e** longe dela (`11`, `150`, para matar `or→and`);
- fronteiras **válidas** `0`, `10`, `100`;
- `presenca` 74 vs 75; `media` 7.0 / 6.9; 5.0 / 4.9;
- uma chamada que cai em cada `return` (inclusive `"Reprovado por falta"` e `"Recuperacao"`), com `==` exato;
- mensagem conferida com `str(exc.value) == "..."`.

Resultado: **36 gerados, 36 mortos, 0 vivos**. **Nenhum mutante equivalente** → **MS = 36/36 = 100 %**.

### d) Trocar a conferência por `pytest.raises(ValueError, match=msg)`

Arquivo: `ex1/variante_d/test_classificacao_match.py` (fora de `tests/`, para não rodar junto).

- Resultado: **34/36 mortos, 2 vivos → MS = 94,4 %**. Sobrevivem `mutmut_7` (`"XXMedia invalidaXX"`) e `mutmut_16` (`"XXPresenca invalidaXX"`).
- Por quê: `match=` usa **`re.search`**, ou seja, procura o padrão *em qualquer parte* da mensagem. `"XXMedia invalidaXX"` ainda contém `"Media invalida"`, então o teste passa.
- Os demais mutantes de mensagem continuam mortos: `None` vira `"None"` (não casa), e minúsculas/maiúsculas não casam porque a busca diferencia caixa.
- Correção: ancorar (`match=f"^{msg}$"`, preferivelmente com `re.escape(msg)`) ou voltar a `str(exc.value) == msg`. Com âncoras: 36/36 de novo (verificado).
- Lição: o *oracle* do teste importa tanto quanto a entrada; uma asserção "frouxa" deixa vivos que a cobertura nunca revela.

---

## Exercício 2 — Desconto Progressivo

### a) Cobertura e MS (suíte: `assert total_com_desconto([10,20,30,40,50]) > 0`)

- Cobertura de ramos: **100 %** (7 comandos, 4 ramos, nada faltando).
- mutmut: **16 gerados, 4 mortos, 12 vivos → MS = 25 %**.
- O que dizem os dois números: a suíte **executa tudo** (cobertura mede *execução*), mas **verifica quase nada** (MS mede *verificação*). O `> 0` é um *oracle* fraco. Os 4 mortos só morrem porque produzem exceção (`total=None`, `enumerate(None)`, `round(None, 2)`) ou total negativo (`-=` no desconto).

### b) `assert` trocado pelo valor exato, mesma entrada

`10 + 20 + 30 + 40·0,9 + 50·0,9 = 141.0` → `assert total_com_desconto([10,20,30,40,50]) == 141.0`

Restam **3 vivos** (13/16 mortos = 81,25 %), todos na linha do `round`:

| Mutante | Mudança |
|---|---|
| `mutmut_13` | `round(total, None)` |
| `mutmut_15` | `round(total, )` (equivale a `round(total)`) |
| `mutmut_16` | `round(total, 3)` |

(O `assert` exato já matou `i > 3`, `i >= 4`, `total = 1`, `+=`→`=`, `/0.9`, `1.9`, `-=` etc.)

### c) Qual condição falhou (Alcançar · Infectar · Propagar · Revelar)

Em todos a linha do `return` **é alcançada**. A causa raiz é a mesma: todos os preços são inteiros e o total é `141.0`, então o arredondamento a 2 casas **não tem nada para arredondar**.

| Vivo | Alcançar | Infectar | Propagar | Revelar |
|---|---|---|---|---|
| 16 `round(total, 3)` | ✔ | ✘ — `round(141.0, 3)` = `141.0`, **mesmo estado** | — | — |
| 13 / 15 `round(total)` | ✔ | só no **tipo**: devolve `141` (`int`) em vez de `141.0` (`float`); o valor numérico não muda | ✔ (o `int` chega à saída) | ✘ — o oracle `==` não distingue: `141 == 141.0` é `True` |

Leitura estrita (infecção = valor diferente): os três falham em **infectar**. Leitura que considera o tipo como parte do estado: 13/15 falham em **revelar**. De qualquer forma, a cura é uma entrada com casas decimais.

### d) Entradas que faltavam

`assert total_com_desconto([10, 20, 30, 10.51]) == 69.46`

- `10 + 20 + 30 + 10,51·0,9 = 69,459` → `round(…, 2) = 69.46`
- `round(x, 3)` daria `69.459`; `round(x)`, `round(x, None)` e `round(x, )` dariam `69`. Uma única entrada mata os três.
- **Tipo de preço necessário: preço com centavos (não inteiro)**, cujo item com desconto gera uma **3ª casa decimal**.
- Resultado: **16/16 mortos, MS = 100 %**. (Mantive 2 testes extras de especificação: 3 itens sem desconto e lista vazia; o MS já era 100 % sem eles.)

---

## Exercício 3 — Temperaturas da Semana

### a) Suíte e vivos

Suíte inicial: 8 testes (3 listas × 2 funções com valor exato + lista vazia com `pytest.raises(ValueError)` sem mensagem).
Cobertura de ramos **100 %**. mutmut: **22 gerados, 11 mortos, 11 vivos** (MS bruto 50 %).

Vivos (`mutmut show`):

| Função | Mutante | Mudança |
|---|---|---|
| `maior` | 2 | `ValueError(None)` |
| `maior` | 3 | `ValueError("XXlista vaziaXX")` |
| `maior` | 4 | `ValueError("LISTA VAZIA")` |
| `maior` | 7 | `temps[1:]` → `temps[2:]` |
| `maior` | 8 | `if t > m` → `if t >= m` |
| `dia_do_maior` | 2, 3, 4 | idem mensagem (`None`, `XX…XX`, maiúsculas) |
| `dia_do_maior` | 9 | `range(1, len(temps))` → `range(len(temps))` |
| `dia_do_maior` | 11 | `range(1, …)` → `range(2, …)` |
| `dia_do_maior` | 12 | `if temps[i] > temps[pos]` → `>=` |

### b) Equivalente ou não?

| Mutante | Veredito | Justificativa |
|---|---|---|
| `maior_2/3/4`, `dia_do_maior_2/3/4` (mensagens) | **Não equivalentes** | A mensagem da exceção é comportamento observável (`str(exc.value)`). Sobrevivem porque a suíte inicial não confere a mensagem. |
| `maior_7` (`[2:]`) | **Não equivalente** | `[21, 30]` devolve `21` no mutante e `30` no original. Sobrevive porque nas listas da suíte o máximo nunca está na posição 1. |
| `maior_8` (`>=`) | **EQUIVALENTE** | Só muda o caminho quando `t == m`; nesse caso `m = t` atribui um valor igual ao que `m` já tem. O valor devolvido é idêntico para qualquer entrada. (Ressalva pedante: com `[1, 1.0]` o *tipo* devolvido mudaria, mas `1 == 1.0`; para a especificação "devolve a maior temperatura" é irrelevante.) |
| `dia_do_maior_9` (`range(len)`) | **EQUIVALENTE** | A iteração extra `i = 0` compara `temps[0] > temps[0]`, que é sempre falso; `pos` não muda. |
| `dia_do_maior_11` (`range(2, …)`) | **Não equivalente** | `[21, 30, 19]`: original → `1`; mutante → `0`. |
| `dia_do_maior_12` (`>=`) | **Não equivalente** | `[30, 21, 30]`: original → `0` (primeiro dia); mutante → `2` (último). Viola "primeiro dia com a maior temperatura". |

**2 equivalentes** (`maior_8`, `dia_do_maior_9`) e **9 não equivalentes**.

### c) Matando os não equivalentes

Testes acrescentados (ver `ex3/tests/test_temperaturas.py`):

- `str(exc.value) == "lista vazia"` para as duas funções;
- `maior([21, 30]) == 30`;
- `dia_do_maior([21, 30, 19]) == 1`;
- `dia_do_maior([30, 21, 30]) == 0` (empate).

| | Gerados | Mortos | Equivalentes | MS |
|---|---|---|---|---|
| Antes | 22 | 11 | 2 | 11/(22−2) = **55 %** (bruto 50 %) |
| Depois | 22 | 20 | 2 | 20/(22−2) = **100 %** (bruto 90,9 %) |

O mutmut ainda lista 2 vivos — exatamente os dois equivalentes, confirmando a análise.

### d) Por que `>` → `>=` é equivalente numa função e não na outra

Depende **do que a função devolve** e **do que a especificação exige**.

- `maior` devolve o **valor**. Num empate, trocar `m` por `t` coloca em `m` um número igual ao anterior: nada observável muda.
- `dia_do_maior` devolve a **posição**. Num empate, o `>=` sobrescreve `pos` com o índice posterior, e a função passa a devolver o **último** dia do máximo, não o **primeiro** como a especificação manda. Um empate (`[30, 21, 30]`) revela a diferença.

A mesma troca textual, duas semânticas diferentes: equivalência não se decide olhando o mutante, e sim o contrato.

---

## Exercício 4 — Parcelamento

### a) Suíte derivada por valor-limite (antes de rodar ferramenta)

Partições de `n`: `n < 1` (inválido) | `1..3` (sem juros) | `4..12` (2 % por parcela além da 3ª) | `n > 12` (inválido).
Valores-limite: **0, 1, 2 | 2, 3, 4 | 11, 12, 13**. Com `valor = 100`:

| n | Resultado esperado (pela especificação) |
|---|---|
| 0 e 13 | `ValueError("parcelas invalidas")` |
| 1 | 100.0 |
| 2 | 50.0 |
| 3 | 33.33 (sem juros) |
| 4 | 102 / 4 = 25.5 (juros 2 %) |
| 11 | 116 / 11 = 10.55 (juros 16 %) |
| 12 | 118 / 12 = 9.83 (juros 18 %) |

A suíte inicial (8 casos) está no começo de `ex4/tests/test_parcelamento.py`; para a mensagem usei `pytest.raises(ValueError, match="parcelas invalidas")`.

### b) Cobertura e MS

- Cobertura de ramos: **100 %** (8 comandos, 4 ramos).
- mutmut: **27 gerados, 25 mortos, 2 vivos → MS = 25/27 = 92,6 %.**
- Confirma a síntese: valor-limite já mata a maior parte dos mutantes; a mutação mostra o que ficou de fora.

### c) Análise dos vivos

| Mutante | Mudança | Veredito |
|---|---|---|
| `mutmut_7` | `ValueError("XXparcelas invalidasXX")` | **Não equivalente.** Sobrevive pelo mesmo motivo do ex. 1(d): `match=` é `re.search`. Morto com `assert str(exc.value) == "parcelas invalidas"` (teste `test_n_invalido_mensagem_exata`). |
| `mutmut_9` | `if n <= 3` → `if n < 3` | **EQUIVALENTE.** Só `n == 3` muda de ramo, e o `else` calcula `0.02 * (3 − 3) = 0`, exatamente o `juros = 0` do ramo original. Mesmo estado, mesma saída: nenhum teste consegue distinguir. |

**MS final = 26 / (27 − 1) = 100 %.** O mutmut continua listando só o `mutmut_9` como vivo.

### d) Mutante de segunda ordem à mão

Combinei dois mutantes de 1ª ordem, **ambos mortos** pela suíte, em linhas diferentes (`ex4/segunda_ordem/parcelamento_2a_ordem.py`):

- **M10** (linha 4): `if n <= 3` → `if n <= 4`
- **M17** (linha 7): `juros = 0.02 * (n - 3)` → `juros = 0.02 * (n - 4)`

Os dois deslocam o início dos juros em uma parcela, ficam "coerentes" entre si, e por isso são um bom candidato a **mascaramento**.

### e) A suíte mata o de segunda ordem?

**Sim.** Rodando `python segunda_ordem/rodar_2a_ordem.py`:

| Variante | Resultado | Testes que falham |
|---|---|---|
| M10 sozinho | morto | `n=4` |
| M17 sozinho | morto | `n=4`, `n=11`, `n=12` |
| **M10 + M17** | **morto** | `n=4`, `n=11`, `n=12` |

Diferenças numéricas (valor 100): n=4 → 25.5 vs 25.0; n=11 → 10.55 vs 10.36; n=12 → 9.83 vs 9.67. Para `n ≤ 3` o combinado coincide com o original, e é só a partir de `n = 4` que ele diverge.

**Relação com o efeito de acoplamento e Offutt (1992):**

- *Efeito de acoplamento*: falhas complexas (aqui, duas mudanças combinadas) são **acopladas** às simples; um conjunto de testes que detecta as falhas simples tende a detectar também as complexas. Isso é o que justifica gerar só mutantes de **1ª ordem**, o que o mutmut faz.
- Offutt (1992) investigou isso empiricamente: conjuntos de teste que matavam todos os mutantes de 1ª ordem também mataram a imensa maioria (acima de 99 %, segundo o estudo) dos de ordens maiores.
- O nosso caso concorda: M10 + M17 morre exatamente pelos testes que matam M10 e M17 isoladamente. Para confirmar além de um exemplo, `segunda_ordem/estudo_pares.py` combina **todos os pares de mutantes em linhas diferentes**: **305 pares, 305 mortos, 0 vivos**.
- Cautela: o efeito é uma **tendência**, não uma garantia. Dois defeitos podem se cancelar em certas entradas (mascaramento). Aqui a fronteira `n = 4` e as pontas `n = 11/12` do valor-limite impediram isso, mas uma suíte sem essas entradas poderia deixar o par vivo.

---

## Como reproduzir

```bash
pip install pytest==9.1.1 pytest-cov==7.1.0 mutmut==3.8.0
cd ex1   # (ou ex2, ex3, ex4)
pytest -q --cov=src --cov-branch --cov-report=term-missing
mutmut run
mutmut results --all true
mutmut show classificacao.x_classificar_aluno__mutmut_7
```

> Os arquivos de teste trazem a suíte **inicial** do enunciado no começo e, abaixo, o que foi acrescentado nos itens (c)/(d) (com comentários dizendo qual mutante cada teste mata). Para reproduzir o "antes", comente os testes acrescentados e rode de novo.
