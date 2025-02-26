# Assembly - Primeiras instruções
## MOV, ADD, INC e DEC

```asm
;Comando MOV
MOV A, #08 ;Move o valor 8 para o Acc
MOV R1, #5 ;Move o valor 5 para o R1
MOV 20H, A ;Move o valor do Acc para o endereço de memória 20H
MOV R2, 20H ;Move o valor de 20H para o R2
MOV 22H, #15 ;Move o valor 15 para o endereço 22H
```

```asm
;Comando ADD
MOV A, #05
ADD A, #03
```

```asm
;Comando DEC e INC
INC A
DEC A
```

```asm
;Exemplos (1)
MOV R0, #10H ;a) sem o 'H' considera como decimal
MOV A, R0 ;b)
MOV 50h, #20H ;c)
INC R2 ;d)
DEC A ;e)
MOV A, #0H ;f)
```

```asm
;(2)
;a) A = A + R0
MOV A, #5H
MOV R0, #2H
ADD A, R0

;b) A = R3 + R2
MOV A, #2H
MOV R3, #1H
MOV R2, #3H
ADD A, R3
ADD A, R2

;c) A = R5 + 30
MOV A, #0H
MOV R5, #10H
ADD A, R5
ADD A, #30H

;d) A = R1 – 1
MOV A, #0H
MOV R1, #7H
ADD A, R1
DEC A

;e) R2 = 31 + R1
MOV R1, #5H
MOV A, R1
ADD A, #31H
MOV R2, A

;f) R2 = R0 + R1 (com acesso indireto aos valores de R0 e R1)
MOV R0, #15H
MOV R1, #10H
MOV 15H, #5H
MOV 10H, #10H
MOV A, @R0 ;@ age como ponteiro
ADD A, @R1
```

```asm
;(3)
;Escreva um código que coloque cada digito do seu número de matrícula na memória de dados iniciando no endereço 20h.
;12345678-9
MOV 20H, #1
MOV 21H, #2
MOV 22H, #3
MOV 23H, #4
MOV 24H, #5
MOV 25H, #6
MOV 26H, #7
MOV 27H, #8
MOV 28H, #9
```
