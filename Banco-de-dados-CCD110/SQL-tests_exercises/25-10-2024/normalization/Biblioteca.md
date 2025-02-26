# Tabela Original
**Livro** (<u>cod_livro</u>, titulo, cod_editora, nome_editora, endereco_editora, *{cod_autor, nomeautor}*)

## ===1FN===

**LIVRO** (<u>cod_livro</u>, titulo, cod_editora, nome_editora, endereco_editora, cod_autor __(FK)__)  
**AUTORIA** (<u>cod_autor</u>, nomeautor)

**DFs**:
- <u>cod_livro</u> -> titulo, cod_editora, cod_autor
- <u>cod_editora</u> -> nome_editora, endereco_editora

## ===3FN===

**LIVRO** (<u>cod_livro</u>, titulo, cod_editora __(FK)__, cod_autor __(FK)__)  
**AUTORIA** (<u>cod_autor</u>, nomeautor)  
**EDITORA** (<u>cod_editora</u>, nome_editora, CEP __(FK)__)  
&emsp;[endereco_editora não está definido no enunciado, então não é obrigatório dividir]*  
**ENDERECO** (<u>CEP</u>, logradouro, complemento, bairro, cidade, estado)*

## ===4FN===

**LIVRO** (<u>cod_livro</u>, titulo, cod_editora __(FK)__)  
**AUTORIA** (<u>cod_livro</u>, <u>cod_autor</u>)  
**AUTOR** (<u>cod_autor</u>, nomeautor)  
**EDITORA** (<u>cod_editora</u>, nome_editora, endereco_editora)