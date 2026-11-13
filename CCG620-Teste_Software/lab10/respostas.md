# Lab 10 – Respostas

Conferido executando os testes contra uma solução minha (pytest 9.1.1, pytest-cov 7.1.0, mutmut 3.8.0). Os números de cobertura e de mutação abaixo são os que obtive; refaça no seu ambiente e relate os seus.

Convenção: teste que já nasce verde não é RED. Use um prefixo próprio (aqui, TEST:) e avise na entrega, pois o enunciado só prevê RED, GREEN e REFACTOR.

---

## Exercício 1 – Contador de palavras (arquivo de testes: ex1/tests/test_contador.py)

### a) Lista ordenada

| # | Caso | O que exige |
|---|------|-------------|
| 1 | "" dá {} | caso degenerado |
| 2 | "teste" dá {"teste": 1} | primeiro resultado não vazio |
| 3 | "bom dia" dá 2 itens | separar palavras |
| 4 | "dia a dia" dá dia 2, a 1 | acumular contagem |
| 5 | "Dia dia DIA" dá {"dia": 3} | normalizar caixa |
| 6 | "fim. Fim!" dá {"fim": 2} | tirar pontuação das bordas |
| 7 | ",dia, ;dia;" dá {"dia": 2} | pontuação nas duas bordas |
| 8 | ":dia: ?dia?" dá {"dia": 2} | demais sinais |
| 9 | "... !" dá {} | token que fica vazio não conta |
| 10 | "bom\ndia" dá 2 itens | quebra de linha separa |
| 11 | três espaços entre bom e dia | espaços repetidos |
| 12 | "guarda-chuva" dá 1 item | hífen interno fica |

Duas primeiras posições: o "" é a entrada mais degenerada; o menor código que passa devolve um dict vazio e fixa o tipo de retorno. O "teste" é o menor caso com conteúdo e triangula o primeiro: devolver sempre vazio deixa de bastar, então o código é forçado a olhar a entrada.

### b) Ciclos

| # | Fase | Resultado | Passo mínimo de produção |
|---|------|-----------|--------------------------|
| 1 | RED, GREEN | falha, passa | devolver dict vazio |
| 2 | RED, GREEN | falha, passa | texto vazio devolve vazio; senão, {texto: 1} |
| 3 | RED, GREEN | falha, passa | separar com split() e contar 1 para cada |
| 4 | RED, GREEN | falha (dia vale 1), passa | acumular com get(palavra, 0) + 1 |
| 5 | RED, GREEN | falha, passa | lower() em cada palavra |
| 6 | RED, GREEN | falha, passa | strip dos seis sinais nas bordas |
| 7 | TEST: | passa de primeira | nenhum |
| 8 | TEST: | passa de primeira | nenhum |
| 9 | RED, GREEN | falha ({"": 2}), passa | ignorar palavra que ficou vazia |
| 10 a 12 | TEST: | passam de primeira | nenhum |
| – | REFACTOR | verde, verde | remover a guarda de texto vazio (redundante) e extrair a constante dos sinais |

### c) git log --oneline

Nenhum GREEN veio sem RED antes. Os testes que já nasceram verdes aparecem como TEST:, para o histórico não mentir. Se o seu log tiver GREEN sem RED imediatamente antes, ou o teste já passava (então não era RED) ou você escreveu código sem teste que o exigisse.

### d) Passaram de primeira

Testes 7, 8, 10, 11 e 12 (neste caminho; depende da sua implementação).
- 7 e 8: strip com o conjunto dos seis sinais já remove todos, nas duas bordas, desde o teste 6.
- 10, 11, 12: split() sem argumento separa por qualquer espaço em branco e descarta vazios; strip só mexe nas bordas, então o hífen interno sobrevive.
Ficam na suíte: não guiaram código, mas documentam o contrato e protegem contra regressões plausíveis (split(" ") no lugar de split(), rstrip no lugar de strip, conjunto de sinais menor). Se você usou split(" ") no ciclo 3, os testes 10 e 11 teriam falhado de primeira e virado RED/GREEN.

### e) Medição

Comandos: pytest --cov=src --cov-branch --cov-report=term-missing -q ; mutmut run ; mutmut results

- Cobertura de ramos obtida: 100%.
- Mutação obtida: 12 de 12 mutantes mortos (100%).
- Limite do escore: no mutmut 3.8.0, constantes de módulo ficam fora da mutação, então o conjunto de sinais não é avaliado. Quem protege o contrato dos seis sinais são os testes 6, 7 e 8; o escore não mostra isso.
- Cobertura de 100% não garante teste bom: diz que a linha executou, não que o resultado foi verificado.

---

## Exercício 2 – Fila de atendimento (testes: ex2/tests/test_fila.py)

### a) Lista de testes (14 itens)

1. Fila nova: aguardando é 0.
2. emitir("normal") devolve "N1".
3. Duas normais: N1, N2.
4. Numeração independente por tipo: normal, prioritária, normal, prioritária dá N1, P1, N2, P2.
5. Tipo inválido lança ValueError e não entra na fila.
6. aguardando conta emitidas e desconta chamadas.
7. chamar() com fila vazia lança IndexError.
8. Ordem de chegada dentro do tipo (N1, depois N2).
9. Prioritária passa na frente (emitidas N1, P1: chama P1).
10. Ordem de chegada entre prioritárias (P1, P2).
11. Depois de 2 prioritárias seguidas, com normal esperando, chama normal: N1,P1,P2,P3 dá P1,P2,N1,P3.
12. A contagem zera depois de chamar normal: N1,N2,P1..P5 dá P1,P2,N1,P3,P4,N2,P5.
13. O limite de 2 não vale sem normal esperando: P1,P2,P3 dá P1,P2,P3.
14. A contagem vale mesmo se a normal chegou depois: P1,P2 chamadas; emite N1; chama N1.

### b) Ciclos

| # | Teste | Fase | Passo mínimo de produção |
|---|-------|------|--------------------------|
| 1 | fila nova | RED, GREEN | classe com aguardando devolvendo 0 |
| 2 | primeira normal | RED, GREEN | emitir devolve "N1" fixo |
| 3 | N1, N2 | RED, GREEN | contador de normais |
| 4 | numeração por tipo | RED, GREEN | contadores por tipo e prefixo N ou P |
| 5 | tipo inválido | RED, GREEN | validar o tipo e lançar ValueError |
| 6 | aguardando | RED, GREEN | uma deque por tipo; aguardando soma os tamanhos |
| 7 | fila vazia | RED, GREEN | lançar IndexError se não há ninguém |
| 8 | ordem de chegada | RED, GREEN ou TEST: | popleft |
| 9 | prioritária na frente | RED, GREEN | olhar prioritárias antes |
| 10 | ordem nas prioritárias | TEST: | passa de primeira |
| 11 | 2 seguidas dá normal | RED, GREEN | contador de seguidas, limite 2 |
| 12 | zerar contagem | RED, GREEN | zerar ao chamar normal |
| 13 | sem normal esperando | RED, GREEN | limite só vale se há normal |
| 14 | normal chegou depois | TEST: | passa de primeira |

No ciclo 13 o RED acontece porque, com o GREEN do 11, P1,P2,P3 tenta tirar uma normal na terceira chamada e dá IndexError.

### c) Qual teste obrigou a quê?

- Contar prioritárias seguidas: o teste 11. Sem contador, "prioritária sempre na frente" devolveria P1,P2,P3,N1.
- Zerar a contagem: o teste 12. Sem o zerar, depois de N1 o contador continuaria em 2 e a quarta chamada devolveria N2 em vez de P3.

### d) Limite de 2 sem normal esperando

O teste 13. Ele obriga a condição "ou não há normal esperando". O teste 14 complementa: a contagem segue valendo e a normal só cobra a vez quando existe.

### e) mutmut

- Cobertura de ramos obtida: 100%.
- Mutação obtida: 49 de 53 mortos (92%).
- Os 4 sobreviventes estavam todos em mensagens de erro (o texto de ValueError e de IndexError). Os testes usam pytest.raises sem match e a especificação não fixa mensagem, então isso não indica comportamento sem teste. Se quiser fixá-las, use match.
- Mutantes na regra (limite, incremento, zerar, ou/e) foram todos mortos pelos testes 9, 11, 12 e 13.
- O limite 2 como literal dentro do método é mutável; como constante de módulo ficaria fora da mutação (slide 4).

---

## Exercício 3 – Carrinho (testes: ex3/tests/test_carrinho.py)

### a) Testes que contradizem as regras novas

- "Cupom em 5000 dá 4500": 5000 está abaixo do mínimo de 10000; o novo total é 5000.
- "1000 após o cupom dá 900": 1000 está abaixo do mínimo; o novo total é 1000.

Continuam válidos: vazio 0; 2500; quantidade=2 dá 5000; preço 0 rejeitado; "XYZ" rejeitado.

O que fazer antes de mexer no código: atualizar esses dois testes para a regra nova, confirmar que falham (isso é o RED) e só então mudar a produção. Não apagar, não marcar skip ou xfail, não corrigir o código primeiro: o teste é a especificação executável. Antes, confirme a base verde com o carrinho da teoria e faça um commit de partida.

### b) Ciclos (uma regra por vez)

| # | Regra | RED | GREEN |
|---|-------|-----|-------|
| 1 | DEZ só a partir de 10000 | reescrever os 2 testes antigos; 9999 dá 9999 e 10000 dá 9000 | se há desconto e subtotal abaixo de 10000, devolver o subtotal (valor fixo, fake it) |
| 2 | VINTE 20% a partir de 30000 | VINTE em 30000 dá 24000; em 29999 dá 29999 | VINTE em CUPONS; um dicionário de mínimos; guardar o mínimo no cupom aplicado |
| 3 | segundo cupom substitui o primeiro | TEST: três testes, já passam | nenhum |
| 4a | quantidade pelo menos 1 | 0 e -1 lançam ValueError | rejeitar quantidade menor que 1 |
| 4b | quantidade inteira | 1.5, 2.0, "2" e True lançam ValueError | checar o tipo antes da comparação |
| – | REFACTOR | verde, verde | porcentagem e mínimo juntos em CUPONS |

Os testes do ciclo 3 passam de primeira porque aplicar_cupom atribui os dois campos, então o último cupom sempre vence. O mais valioso: DEZ e depois VINTE com subtotal 10000 deve dar 10000, o que separa "substitui" de "fica com o melhor desconto".

Dois testes vieram da análise de mutação, não da leitura da especificação: preço 1 é aceito (fronteira de preço; mata o mutante que troca preço <= 0 por preço <= 1) e várias adições acumulam (mata o mutante que troca += por =; o teste do cupom antes de adicionar passava por coincidência).

### c) REFACTOR: o que mostra que nada mudou?

- A suíte estava verde antes e continua verde depois, sem editar nenhum teste. O git diff --stat do commit REFACTOR só pode listar o arquivo de produção.
- Os testes só usam a API pública (adicionar, aplicar_cupom, total). Se algum acessasse CUPONS ou o campo interno do desconto, a refatoração o quebraria: sinal de teste acoplado à implementação.

### d) Valores de quantidade testados

| Valor | Classe ou fronteira | Motivo |
|-------|---------------------|--------|
| 1 | menor válido | fronteira inferior |
| 2 | válido típico | já existia (quantidade=2 dá 5000) |
| 0 | primeiro inválido | fronteira |
| -1 | negativo | classe distinta de zero |
| 1.5 | float não inteiro | passaria se só houvesse a comparação com 1 |
| 2.0 | float de valor inteiro | decisão minha: "inteira" = tipo int; confirme com o professor |
| "2" | tipo errado | exige checar o tipo antes de comparar |
| True | bool é subclasse de int | decisão minha: rejeitar; sem o teste passaria como 1 |

### Medição (extra)

- Cobertura de ramos obtida: 100%. Mutação obtida: 16 de 25 mortos (64%).
- Os 9 sobreviventes estavam todos em mensagens de erro (sem importar para a especificação).
- No mutmut 3.8.0, o corpo de total (uma @property) fica fora da mutação. O escore não avalia as regras de cupom; quem as protege são os testes de fronteira (9999/10000, 29999/30000) e de substituição.

---

## Resumo

- O histórico do Git mostra se o ciclo foi seguido: RED antes de cada GREEN. Teste que já nasce verde não é RED.
- Teste que passa de primeira não guiou código, mas documenta o contrato e fica.
- Regra nova muda primeiro o teste, depois o código, depois limpa (REFACTOR com suíte verde antes e depois).
- Cobertura e mutação altas tendem a vir do TDD, sem garantia: fronteiras, constantes de módulo e @property dependem da sua lista de testes.
