# Exercícios Aula Lab

## Exercício 1
Em uma atividade da aula vocês leram na documentação do Arduino UNO que ele possuí 32KB de memória flash (memória do programa) e 2KB de memória RAM. Sabendo dessas informações responda as perguntas abaixo:

	a) Qual o tamanho máximo de elementos de um vetor do tipo char que  você pode declarar, considerando que não haverá nenhuma outra variável? 
		char vetor[ ? ];
	b) Qual o tamanho máximo de elementos de um vetor do tipo int que você pode declarar, considerando que não haverá nenhuma outra variável, sabendo que o int no Arduino é de 16bits? 
		int vetor[ ? ];

**Respostas**:
	
	a) char = 1 byte na memória RAM; tamanho da memória RAM = 2048 bytes
		char vetor[2048];
	b) int = 2 bytes; tamanho da memória RAM = 2048 bytes
		int vetor[1024];

## Exercício 2
Represente o número -20 usando o padrão complemento de 2 em 8 bits. Apresente todos os cálculos realizado para a conversão. Apresente o valor representado pela calculadora do programador (print da tela).

_Obs: Não será aceito como resposta apenas o valor final em binário, precisa apresentar todos os cálculos realizado_

**Resposta**:

> $20_{10} = 0001.0100_{2}$
> 
> Complemento de dois: _Inverter o valor em binário e somar 1_
>
> $1110.1011_2 + 0000.0001_2 = 1110.1100_2$

Com a calculadora de programador do Windows, ele calcula em 64 bits:

![image](https://github.com/user-attachments/assets/6e228476-45c9-4958-a1f5-a0bbaea897d5)


## Exercício 3
Verifique se sua resposta do exercício anterior está correta realizando a programação em C++ e observando a representação do número -20.

**Resposta**:

## Exercício 4
Quando você declara uma variável do tipo **int** no Arduino UNO, ele usa apenas  2 Bytes para armazenamento do conteúdo da variável.

Qual faixa de números que podemos representar em uma variável do tipo **int** no Arduino UNO?

**Resposta**: Como estamos tratando inteiros sinalizados (negativos e positivos), temos 2 bytes, ou seja, 16 bits para representá-los, sendo o mais significativo de sinal -> $2^{15} = 32.768$, sendo negativo e positivo. Ou seja, de -32.768 a 32.767, num total de 32.766 números.

## Exercício 5
Quanto você declara uma variável do tipo **long** no Arduino UNO, ele usa 4 bytes para armazenamento do conteúdo da variável.

Qual faixa de números inteiros que podemos representar em uma variável do tipo **long** no Arduino UNO?

**Resposta**: Como estamos tratando inteiros sinalizados (negativos e positivos) long, temos 4 bytes, ou seja, 32 bits para representá-los, sendo o mais significativo de sinal -> $2^{31} = 2.147.483.648$, sendo negativo e positivo. Ou seja, de -2.147.483.648 a 2.147.483.648, num total de 2.147.483.646 números.

## Exercício 6
Quando você declara uma variável do tipo **unsigned int** no Arduino UNO, ele usa apenas 2 bytes para armazenamento do conteúdo da variável.

Qual faixa de números que podemos representar em uma variável do tipo **unsigned int** no Arduino UNO?

**Resposta**: Como estamos tratando inteiros não sinalizados (apenas positivos), temos 2 bytes, ou seja, 16 bits para representá-los -> $2^{16} = 65.536$. Ou seja, de 0 a 65.536.

## Exercício 7
Quando você declara uma variável do tipo **unsigned long** no Arduino UNO, ele usa 4 bytes para armazenamento do conteúdo da variável.

Qual faixa de números que podemos representar em uma variável do tipo **unsigned long** no Arduino UNO?

**Resposta**: Como estamos tratando inteiros não sinalizados (apenas positivos) long, temos 4 bytes, ou seja, 32 bits para representá-los -> $2^{32} = 4.294.967.296$. Ou seja, de 0 a 4.294.967.296.

## Exercício 8
Quando você declara uma variável do tipo **long long** no Arduino UNO, ele usa apenas 8 bytes para armazenamento do conteúdo da variável.

Qual faixa de números que podemos representar em uma variável do tipo **long long** no Arduino UNO?

**Resposta**: Como estamos tratando inteiros sinalizados (negativos e positivos) long long, temos 8 bytes, ou seja, 64 bits para representá-los -> $2^{63} = 9.223.372.036.854.775.808$, sendo negativo e positivo. Ou seja, de -9.223.372.036.854.775.808 a 9.223.372.036.854.775.807, num total de 9.223.372.036.854.775.806 números.

## Exercício 9
Sabemos que uma variável do tipo int no Arduino UNO ocupa 16 bits. Portanto, represente em binário o número armazenado na variável do programa abaixo:
	
```cpp
int valor = -52;
```

**Resposta**:
> $52_{10} = 0011.0100_{2}$
> 
> Complemento de dois: _Inverter o valor em binário e somar 1_
>
> $1100.1011_2 + 0000.0001_2 = 1100.1100_2$
>
> Em 16 bits: $1111.1111.1100.1100_2$

## Exercício 10
Explique o que é **overflow** e **underflow** em relação à representação de números inteiros (apresente exemplos do underflow e overflow de números inteiros de 32bits).

**Resposta**: Overflow é quando o número estoura o limite de bits pra cima, ou seja, números positivos; underflow é o mesmo mas para baixo, números negativos.

```cpp
long valor = 2147483648 //overflow com inteiro do tipo long (32 bits)
long valor = -2147483649 //underflow com inteiro do tipo long (32 bits)
```

## Exercício 11
Represente em binário o número **43** utilizando a representação excessiva em máquinas de 8 bits usando um bias de 127.

**Resposta**:
> $127+43=170_{10}$
> 
>$170_{10} = 1010.1010_2$

## Exercício 12
Represente em binário o número **-20** utilizando a representação excessiva em máquinas de 8 bits usando um bias de 127.

**Resposta**:
> $127-20=107_{10}$
> 
> $107_{10} = 0110.1011_2$

## Exercício 13
Converta os números abaixo para hexadecimal:
	
- $10011110_2$ = $\text{9E}_{16}$

- $10111010_2$ = $\text{BA}_{16}$

- $1100110110000011_2$ = $\text{CD83}_{16}$
