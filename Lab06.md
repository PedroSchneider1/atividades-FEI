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
MOV R7, #25 		;seta os valores nos registradores
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

# Exercícios Aula Lab

## Exercício 1
Verifique quais instruções não são executadas nesse código.

![image](https://github.com/user-attachments/assets/7b4c04ae-6ef6-4bd3-9bb7-8d168352b2a3)

## Exercício 2
Crie um programa que fique alternando a rotação a esquerda e rotação a direita na porta P1, faça com que essa rotação seja alternada a cada 1 volta completa.

```asm
MOV A, #11111110b
MOV R0, #7
MOV P1, A

LEFT:
	RL A
	MOV P1, A
	DJNZ R0, LEFT
	MOV R0, #7	
	SJMP RIGHT

RIGHT:
	RR A
	MOV P1, A
	DJNZ R0, RIGHT
	MOV R0, #7
	SJMP LEFT
```

## Exercício 3
Coloque cada dígito do seu número de matricula na memória iniciando no endereço 30h (cada número em um byte da memória).
Escreva uma subrotina que contém um laço de repetição que copie os valores do vetor iniciando no endereço 30h para um outro vetor iniciando no endereço 40h.
Termine o programa com um laço infinito.
Obs: crie a sub-rotina main e dentro da main chame a sub-rotina de cópia.

```asm
;N° 12.345.678-9
;coloca os números no vetor a partir de 30h
MOV 30h, #1
MOV 31h, #2
MOV 32h, #3
MOV 33h, #4
MOV 34h, #5
MOV 35h, #6
MOV 36h, #7
MOV 37h, #8
MOV 38h, #9

;inicializa os apontadores
MOV R0, #30h 		;apontador para o vetor origem
MOV R1, #40h 		;apontador para o vetor destino

MAIN:
    LCALL COPY 		;chama a sub-rotina de cópia
    SJMP $     		;laço infinito

COPY:
    MOV R2, #9 		;tamanho do vetor (9 elementos)
COPIAR:
    MOV A, @R0 		;carrega o valor da memória apontada por R0 em A
    MOV @R1, A 		;copia o valor de A para o endereço apontado por R1
    INC R0     		;incrementa o apontador de origem
    INC R1     		;incrementa o apontador de destino
    DJNZ R2, COPIAR 	;decrementa R2 e repete o laço até R2=0
    RET        		;retorna para a MAIN

```

## Exercício 4
Teste e verifique o que faz esse programa, observe o valor do SP e o que está sendo armazenado na Pilha.

```asm
Principal:
	MOV A, #11h
	ACALL FUNC01
	SJMP $

org 1100h
FUNC01:
	MOV 30H, #33h
	ACALL FUNC02
	NOP
	RET

org 2130h
FUNC02:
	MOV 40H, #01H
	ACALL FUNC03
	NOP
	RET
org 30A0h

FUNC03:
	MOV 40H, #50H
	RET
```

```c
/*
Como estamos trabalhando com funções, o processador precisa guardar na pilha qual endereço de retorno
depois de chamar uma função, o Stack Pointer (SP) aponta o topo da pilha, ou seja, onde na memória está
o último endereço de retorno da última chamada de função.
*/
```

## Exercício 5
Funções iterativas são funções que utilizam estruturas de controle de fluxo iterativas, como loops, para repetir uma  sequência de instruções até que uma condição seja atendida.
Qual é a diferença entre uma função recursiva e uma função iterativa em termos de desempenho e consumo de memória?
- **R.:** Uma função recursiva guarda o endereço de retorno dela mesma na pilha, causando um consumo maior de memória.

## Exercício 6
Qual é o principal problema que pode ocorrer quando criamos funções recursivas em programas? Como podemos evitá-lo?.
- **R.:** Uma recursão infinita. Para evitar, é necessário que qualquer recursão tenha alguma condição de parada.

## Exercício 7
Faça uma função recursiva (sub-rotina recursiva) com o problema que você respondeu no exercício anterior.
Execute o programa e apresente a imagem da Tela do programa executado.

```asm
LJMP MAIN

org 1111h
MAIN:
	LCALL FUNC
	SJMP $

FUNC:
	NOP
	LCALL FUNC
	RET
```

![image](https://github.com/user-attachments/assets/bf7aa91e-c80c-4699-8a9a-d84233e69b3b)


