# Laboratório 9 (Reforço) — Testes de Mutação · Guia de Estudo

Material de estudo do **Lab 9 Reforço** (CCG620 · Teste de Software · FEI), com
**tudo criado e executado de verdade**: código, suítes de teste de cada etapa,
logs do `mutmut` e **respostas didáticas** de todos os itens.

> ⚠️ Como o professor não publicou gabarito, estas respostas foram **produzidas e
> verificadas rodando as ferramentas**, mas são **material de estudo**. Tente resolver
> sozinho primeiro, e só depois compare. Detalhes de interpretação (ex.: mensagens de
> erro como equivalentes ou não) estão sinalizados nas "ressalvas" de cada exercício.

---

## 1. Mapa das pastas

```
lab09b/
├── 00_LEIA_PRIMEIRO.md        ← este guia (conceitos + resumo + como rodar)
├── resumo_numeros.txt         ← gerados/mortos/vivos de cada etapa
├── rodar_tudo.sh              ← refaz TODAS as medições do zero
├── rodar_etapa.sh             ← roda UMA etapa de UM exercício
├── mostrar_mutantes.sh        ← grava o diff (mutmut show) de cada mutante
├── .gitignore                 ← ignora mutants/ (pasta temporária do mutmut)
├── ex1/  ex2/  ex3/  ex4/
│   ├── RESPOSTAS.md           ← respostas didáticas dos itens a), b), c)…
│   ├── pyproject.toml         ← config do mutmut e do pytest
│   ├── src/                   ← código sob teste (do enunciado)
│   ├── tests/                 ← suíte FINAL (a melhor, a que deixa MS = 100 %)
│   ├── etapas/                ← CADA versão da suíte (inicial → … → final)
│   ├── logs/                  ← saídas reais: cobertura, mutmut, diffs dos mutantes
│   └── extras/                ← (ex3, ex4) experimentos de apoio
```

**Ordem sugerida de estudo:** seção 2 (conceitos) → `ex1/RESPOSTAS.md` → `ex2` →
`ex3` → `ex4`. Em cada um, abra `etapas/a_…/` (suíte inicial), leia o diff dos vivos em
`logs/*_5_diffs.txt` e **tente prever** quem sobrevive antes de ler a resposta.

---

## 2. Mini-aula de conceitos

| Termo | Significado |
|---|---|
| **Mutante** | Cópia do programa com **um pequeno defeito inserido de propósito** (`<` → `<=`, `+` → `-`, `0` → `1`, texto trocado…). |
| **Matar** o mutante | Algum teste **falha** quando roda contra o mutante → a suíte "percebeu" o defeito. 🎉 |
| **Mutante vivo (sobrevivente)** | **Todos os testes passam** com o defeito → há uma **lacuna** na suíte. 🙁 |
| **Mutante equivalente** | Programa mutante que se comporta **igual** ao original em **toda** entrada: **não dá** para matar. Fica **fora** do cálculo. |
| **Escore de mutação (MS)** | `MS = mortos / (gerados − equivalentes)` |
| **1ª ordem / 2ª ordem** | 1 mudança / 2 mudanças combinadas no mesmo mutante. |
| **Efeito de acoplamento** | Testes que matam os defeitos simples tendem a matar também os compostos (Offutt, 1992). |

### Modelo RIPR — as 4 condições para matar um mutante

```
 ALCANÇAR  →  INFECTAR  →  PROPAGAR  →  REVELAR
 (Reach)      (Infect)     (Propagate)   (Reveal)
 a linha      o estado     a diferença   o assert
 mutada       interno      chega à       percebe
 roda?        difere?      saída?        a diferença?
```

Se **qualquer** uma falhar, o mutante **sobrevive**. Para cada vivo pergunte:
*qual dos 4 degraus falhou?*

| Degrau que falhou | Remédio típico |
|---|---|
| Alcançar | acrescentar um **teste que passe pela linha** |
| Infectar | escolher **entrada diferente** (fronteira, valor "quebrado", empate…) |
| Propagar | garantir que o valor errado **chegue ao retorno** |
| Revelar | **assert exato** (`== valor`), conferir a mensagem, o tipo… |

### Cobertura × mutação (a grande lição do lab)

- **Cobertura** responde: *"os testes **passaram por** este código?"*
- **Mutação** responde: *"os testes **detectariam um erro** neste código?"*

Exemplo real daqui (ex2): **100 % de cobertura de ramos e só 23 % de mutantes mortos.**

---

## 3. Resumo de todos os números (medidos de verdade)

| Ex. | Etapa | Nº testes | Cobertura de ramos | Gerados | Mortos | Vivos | Equiv. | **MS** |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | `a_inicial` | 2 | **64 %** | 36 | 6 | 30 | 0 | **16,7 %** |
| 1 | `d_match` (`match=`) | 20 | 100 % | 36 | 34 | 2 | 0 | **94,4 %** |
| 1 | `e_match_ancorado` (bônus) | 20 | 100 % | 36 | 36 | 0 | 0 | 100 % |
| 1 | **`c_final`** | 20 | 100 % | 36 | 36 | 0 | 0 | **100 %** |
| 2 | `a_inicial` (`> 0`) | 1 | **100 %** | 13 | 3 | 10 | 0 | **23,1 %** |
| 2 | `b_exato` (`== 15.0`) | 1 | 100 % | 13 | 10 | 3 | 0 | **76,9 %** |
| 2 | **`d_final`** | 5 | 100 % | 13 | 13 | 0 | 0 | **100 %** |
| 3 | `a_inicial` | 8 | 100 % | 22 | 11 | 11 | 2 | **55 %** (11/20) |
| 3 | **`c_final`** | 14 | 100 % | 22 | 20 | 2 (equiv.) | 2 | **100 %** (20/20) |
| 4 | `a_bva` | 10 | 100 % | 26 | 19 | 7 | 1 | **76 %** (19/25) |
| 4 | **`c_final`** | 13 | 100 % | 26 | 25 | 1 (equiv.) | 1 | **100 %** (25/25) |

**Experimento de 2ª ordem (ex4):** 143 + 260 mutantes de 2ª ordem testados,
**0 sobreviveram**.

### Padrões que se repetiram nos 4 exercícios (decore!)

1. 🔹 **Mensagens de exceção** (`ValueError("...")`) → mutmut gera 3–4 mutantes de texto
   (`None`, `XX…XX`, minúscula, MAIÚSCULA). Só morrem se o teste **confere a mensagem**.
2. 🔹 **Fronteiras (`<`, `<=`, `>`, `>=`)** → exigem **um teste de cada lado** da fronteira.
3. 🔹 **`round(x, 2)`** → só morre com um resultado de **mais de 2 casas decimais**.
4. 🔹 **Assert fraco (`> 0`)** deixa vivo quase tudo; **assert exato** resolve a revelação.
5. 🔹 **Equivalentes** costumam ser: `<` ↔ `<=` quando o empate não muda o resultado;
   iterações extras que repetem o valor inicial.

---

## 4. Como rodar tudo (Linux / GitHub Codespaces / WSL)

O `mutmut 3.8.0` **não roda no Windows nativo** (pede WSL); use Codespaces, WSL ou Linux.

```bash
pip install pytest==9.1.1 pytest-cov==7.1.0 mutmut==3.8.0

# Refazer todas as medições (leva alguns minutos):
bash rodar_tudo.sh

# Ou apenas UM exercício, passo a passo (exemplo: ex1):
cd ex1
pytest -q --cov=src --cov-branch --cov-report=term-missing   # testes + cobertura
mutmut run                                                   # gera e testa os mutantes
mutmut results                                               # lista os vivos
mutmut results --all true                                    # lista todos
mutmut show frete.x_modalidade_frete__mutmut_3               # ver a mudança de um mutante
```

Para rodar **uma etapa específica** (ex.: a suíte inicial do ex3):

```bash
./rodar_etapa.sh ex3 a_inicial        # copia etapas/a_inicial/* para tests/ e mede
```

**Dicas que evitam dor de cabeça**

- Antes do `mutmut`, **todos os testes precisam passar** (senão: `failed to collect stats`).
- Se mudar os testes ou o código, apague o cache: `rm -rf mutants` e rode de novo.
- Os **números dos mutantes** (`mutmut_7` etc.) seguem a ordem em que o mutmut 3.8.0
  os gera; com outra versão podem mudar. Os **diffs** em `logs/*_5_diffs.txt` mostram
  exatamente qual mudança cada número representa.
- O `mutants/` é uma pasta temporária: **não** vai para o Git (já está no `.gitignore`).

---

## 5. Roteiro de autoavaliação (feche os arquivos e responda)

1. Por que 100 % de cobertura de ramos pode dar MS baixo? (ex2)
2. O que significa "Revelar" no RIPR e como o `assert` exato ajuda?
3. Por que `match="Peso invalido"` deixa passar `"XXPeso invalidoXX"`? Como corrigir? (ex1)
4. Dê um exemplo de mutante **equivalente** e justifique em 2 linhas. (ex3 ou ex4)
5. Por que `<` → `<=` é equivalente em `menor_preco` e **não** em `dia_da_compra`? (ex3)
6. O que é um mutante de 2ª ordem e o que diz o efeito de acoplamento? (ex4)
7. Como se calcula o MS e por que os equivalentes saem do denominador?

Bons estudos! 🧬
