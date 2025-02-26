# Assembly - Exercícios
```asm
;2) Desenvolva um código para as operações a seguir
;a) Coloque qualquer valor entre 32 e 127 no acumulado
MOV A, #50h

;b) Some no acumulador o valor que está no registrador R1 com o valor do acumulador
MOV R1, #20H
ADD A, R1

;c) Some em R3 o valor que está em R1 com o valor que está em R2
MOV R2, #10H
MOV A, R2
ADD A, R1
MOV R3, A

;d) Incremente o valor que está em R3 e em seguida some em R3 o valor do acumulador
INC R3
ADD A, R3
MOV R3, A
```
