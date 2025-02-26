# Tabela Original

**Movel**(<u>cod_movel</u>, descrição, preco_unit, *{cod_mao_obra, descricao_mo, preco_mo, quantidade_usada_mo}, {cod_materia_prima,descricao_mp,preco_mp,quant_usada_mp}*)  
**mao_obra** (<u>cod_mao_obra</u>,descricao_mao_obra,preco_mao_obra)  
**materia_prima** (<u>cod_materia_prima</u>,descricao_mat_prima,preco_mat_prima)  

## ===1FN===

**MOVE** (<u>cod_movel</u>, descrição, preco_unit)  
**MAO_OBRA** (<u>cod_mao_obra</u>, descricao_mao_obra, preco_mao_obra)  
**MATERIA_PRIMA** (<u>cod_materia_prima</u>, descricao_mat_prima, preco_mat_prima, quant_usada_mp)  

**DFs**:
- <u>cod_movel</u> -> descrição, preco_unit
- <u>cod_mao_obra</u> -> descricao_mao_obra, preco_mao_obra
- <u>cod_materia_prima</u> -> descricao_mat_prima, preco_mat_prima, quant_usada_mp

## ===3FN===

**MOVEL** (<u>cod_movel</u>, descrição, preco_unit)  
**MAO_OBRA** (<u>cod_mao_obra</u>, descricao_mao_obra, preco_mao_obra)  
**MATERIA_PRIMA** (<u>cod_materia_prima</u>, descricao_mat_prima, preco_mat_prima,   quant_usada_mp)  
**MOVEL_MAO_OBRA** (<u>cod_movel</u>, <u>cod_mao_obra</u>, quantidade_usada_mo)  
**MOVEL_MATERIA_PRIMA** (<u>cod_movel</u>, <u>cod_materia_prima</u>, qtt_usada_mp)  