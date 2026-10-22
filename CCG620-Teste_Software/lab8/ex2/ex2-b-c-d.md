## a) Pares por condição

| Condição | Nº de pares |
|---|---|
| `cartao` | 1 |
| `documento` | 1 |
| `grupo_chamado` | 1 |
| `prioridade` | 7 |

## b) Conjuntos MC/DC mínimos

O mínimo é de **5 casos**, e existem **3 conjuntos mínimos distintos** (calculados sobre `regra`). Os pares de `cartao`, `documento` e `grupo_chamado` são únicos e compartilham a linha `TTTF`. Para `prioridade`, há três escolhas que reaproveitam uma linha já existente.

## c) `pode_embarcar` vs `regra` com dois testes

| Entrada | `pode_embarcar` | `regra` | Especificação assumida |
|---|---|---|---|
| todos V | True | True | True |
| todos F | False | False | False |

Os dois testes concordam entre si e com a especificação. O `if` tem as duas saídas cobertas (True e False), então a cobertura de ramos é de **100%**. Esse cálculo foi feito por raciocínio; não rodei o `pytest-cov` nesta etapa.

## d) Quais conjuntos acham o defeito?

**O defeito:** em Python, `and` tem precedência sobre `or`. Então

```python
cartao and documento and grupo_chamado or prioridade
```

é lido como `(cartao and documento and grupo_chamado) or prioridade`. Com isso, **`prioridade` sozinha libera o embarque**, sem cartão nem documento.

Resultado de cada conjunto:

| Conjunto | Detecta? | Motivo |
|---|---|---|
| 1 | Sim | Inclui `FTTT`: `prioridade` True, `cartao` False |
| 2 | Sim | Inclui `TFTT`: `prioridade` True, `documento` False |
| 3 | **Não** | Usa `TTFT`, em que `cartao` e `documento` são True. Aqui as duas versões dão o mesmo resultado |

Ou seja, MC/DC mínimo não garante detectar o defeito. Depende de quais linhas são escolhidas.
