# Exercícios Aula Teórica (fixação)

## Exercício 4
Crie um programa que escreva zero em todas as posições da RAM interna, ou seja, do endereço 0 até o endereço 127 da  RAM interna.
```asm
;RETORNA: posicoes de 0 a 127 da RAM interna zeradas
;USA: A e R0

ZERA:
	CLR A		;A = 0, valor a ser escrito
	MOV R0, #127	;R0 = endereço mais alto
ROT:
	MOV @R0, A	;zera a posição apontada por R0
	DJNZ R0, ROT	;decrementa o ponteiro e contador
```

## Exercício 5
Construir e testar um programa em linguagem assembly que deve carregar (alocar) o valor EEh em 50 bytes consecutivos da RAM interna iniciando no endereço 20h.

```asm
MOV R0, #50
MOV R1, #20h

ROT:
	MOV @R1, #0EEh
	INC R1
	DJNZ R0, ROT
```

## Exercício 6
Compare dois números inteiros sem sinal que estão localizados em R7 e R6. Armazene o maior em R7 e o menor em R6. Termine o programa com um laço infinito.

### Solução em aula:
```asm
MOV R6, #3
MOV R7, #2

MOV A, R7
MOV 20h, R6
CJNE A, 20h, PROXIMO

PROXIMO:
	JNC FIM
	MOV A, R7
	XCH A, R6
	MOV R7, A

FIM:
	NOP
```

### Solução no PDF:
```asm
MOV R7, #25 	;seta os valores nos registradores
MOV R6, #30

COMP:
	MOV A, R7	;coloca o primeiro número no Acc (A = R7)
	CLR C		;zera o carry
	SUBB A, R6	;A - R6, se C = 0 -> A >= R6 (não troca)
				;		 se C = 1 -> A <  R6 (troca)
	
	JNC FIM		;se C = 0, finaliza
	XCH A, R7	;
	XCH A, R6	;troca os conteúdos de R6 e R7
	XCH A, R7	;

FIM:
	SJMP $		;para em um laço infinito
```
