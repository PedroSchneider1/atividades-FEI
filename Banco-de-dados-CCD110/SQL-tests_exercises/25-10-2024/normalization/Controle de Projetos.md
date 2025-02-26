# Tabela Original
**ProjetoEmpr** (<u>cod_proj</u>, tipo, descricao, *{cod_empregado, nome_empregado, categoria_empregado, salario_categoria, data_inicio_projeto, data_fim_projeto}*)

## ===1FN===

**PROJETO** (<u>cod_proj</u>, tipo, descricao)  
**ALOCACAO** (<u>cod_empregado</u>, nome_empregado, categoria_empregado, salario_categoria, data_inicio_projeto, data_fim_projeto)

**DFs**:
- <u>cod_proj</u> -> tipo, descricao
- <u>cod_empregado</u> -> nome_empregado, categoria_empregado, salario categoria, data_inicio_projeto, data_fim_projeto
- <u>categoria_empregado</u> -> salario categoria
- (<u>cod_proj</u>, <u>cod_empregado</u>) -> data_inicio_projeto, data_fim_projeto

## ===3FN===

**PROJETO** (<u>cod_proj</u>, tipo, descricao)  
**CATEGORIA** (<u>categoria_empregado</u>, salario_categoria)  
**ALOCACAO** (<u>cod_proj</u> __(FK)__, <u>cod_empregado</u> __(FK)__, data_inicio_projeto, data_fim_projeto)  
**EMPREGADO** (<u>cod_empregado</u>, nome empregado, categoria empregado __(FK)__)  