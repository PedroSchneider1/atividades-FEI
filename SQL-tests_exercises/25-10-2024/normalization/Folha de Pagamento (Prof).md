# Normalização do Esquema de Funcionários e Pagamentos

## 1. Análise da Estrutura Original

### Tabelas Originais:
```
Funcionario(func_codigo, func_nome, func_endereço, numero_banco, agencia_banco, {func_data_falta, func_motivo_falta})

Pagamento(func_codigo, func_mes, func_ano, valor_depositado)
```

### Identificação dos Atributos

#### Funcionario:
- func_codigo (identificador do funcionário)
- func_nome
- func_endereço
- numero_banco
- agencia_banco
- Grupo repetitivo de faltas:
  - func_data_falta [multivalorado]
  - func_motivo_falta [multivalorado]

#### Pagamento:
- func_codigo
- func_mes
- func_ano
- valor_depositado

## 2. Identificação das Dependências Funcionais (DFs)

### DFs na tabela Funcionario:
1. `func_codigo → func_nome, func_endereço, numero_banco, agencia_banco`
   - O código do funcionário determina seus dados pessoais e bancários

2. `(func_codigo, func_data_falta) → func_motivo_falta`
   - Para cada falta de um funcionário, existe um motivo específico

### DFs na tabela Pagamento:
1. `(func_codigo, func_mes, func_ano) → valor_depositado`
   - A combinação de funcionário, mês e ano determina o valor do pagamento

## 3. Processo de Normalização

### 1ª Forma Normal (1FN)
- Eliminar grupos repetitivos
- Criar tabelas separadas para atributos multivalorados

### 2ª e 3ª Formas Normais (2FN e 3FN)
- Remover dependências parciais
- Separar dados bancários em tabela própria

## 4. Esquema Final Normalizado

```sql
-- Tabela de Funcionários
CREATE TABLE FUNCIONARIO (
    codigo INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(200) NOT NULL
);

-- Tabela de Dados Bancários
CREATE TABLE DADOS_BANCARIOS (
    func_codigo INT PRIMARY KEY,
    numero_banco VARCHAR(10) NOT NULL,
    agencia_banco VARCHAR(10) NOT NULL,
    CONSTRAINT fk_funcionario FOREIGN KEY (func_codigo) 
        REFERENCES FUNCIONARIO(codigo)
);

-- Tabela de Faltas
CREATE TABLE FALTA (
    func_codigo INT,
    data_falta DATE,
    motivo VARCHAR(200) NOT NULL,
    CONSTRAINT pk_falta PRIMARY KEY (func_codigo, data_falta),
    CONSTRAINT fk_funcionario_falta FOREIGN KEY (func_codigo) 
        REFERENCES FUNCIONARIO(codigo)
);

-- Tabela de Pagamentos
CREATE TABLE PAGAMENTO (
    func_codigo INT,
    mes INT CHECK (mes BETWEEN 1 AND 12),
    ano INT,
    valor_depositado DECIMAL(10,2) NOT NULL,
    CONSTRAINT pk_pagamento PRIMARY KEY (func_codigo, mes, ano),
    CONSTRAINT fk_funcionario_pagamento FOREIGN KEY (func_codigo) 
        REFERENCES FUNCIONARIO(codigo),
    CONSTRAINT chk_ano CHECK (ano >= 2000)
);

-- Índices para otimização
CREATE INDEX idx_funcionario_nome ON FUNCIONARIO(nome);
CREATE INDEX idx_falta_data ON FALTA(data_falta);
CREATE INDEX idx_pagamento_periodo ON PAGAMENTO(ano, mes);
```

## 5. Views Úteis

```sql
-- View para relatório de funcionários com dados bancários
CREATE VIEW FUNCIONARIO_COMPLETO AS
SELECT 
    f.codigo,
    f.nome,
    f.endereco,
    db.numero_banco,
    db.agencia_banco
FROM FUNCIONARIO f
LEFT JOIN DADOS_BANCARIOS db ON f.codigo = db.func_codigo;

-- View para relatório de faltas por período
CREATE VIEW RELATORIO_FALTAS AS
SELECT 
    f.codigo,
    f.nome,
    ft.data_falta,
    ft.motivo,
    COUNT(*) OVER (PARTITION BY f.codigo, EXTRACT(MONTH FROM ft.data_falta), 
                   EXTRACT(YEAR FROM ft.data_falta)) as faltas_no_mes
FROM FUNCIONARIO f
JOIN FALTA ft ON f.codigo = ft.func_codigo;

-- View para folha de pagamento
CREATE VIEW FOLHA_PAGAMENTO AS
SELECT 
    f.codigo,
    f.nome,
    p.mes,
    p.ano,
    p.valor_depositado,
    db.numero_banco,
    db.agencia_banco,
    COUNT(ft.data_falta) as total_faltas_mes
FROM FUNCIONARIO f
JOIN PAGAMENTO p ON f.codigo = p.func_codigo
LEFT JOIN DADOS_BANCARIOS db ON f.codigo = db.func_codigo
LEFT JOIN FALTA ft ON f.codigo = ft.func_codigo 
    AND EXTRACT(MONTH FROM ft.data_falta) = p.mes 
    AND EXTRACT(YEAR FROM ft.data_falta) = p.ano
GROUP BY f.codigo, f.nome, p.mes, p.ano, p.valor_depositado, 
         db.numero_banco, db.agencia_banco;
```

## 6. Justificativa das Mudanças

1. **Separação de Dados Bancários:**
   - Informações bancárias em tabela separada
   - Facilita mudança de dados bancários
   - Mantém histórico se necessário

2. **Normalização de Faltas:**
   - Cada falta registrada individualmente
   - Permite múltiplos motivos por dia
   - Facilita relatórios e análises

3. **Estrutura de Pagamentos:**
   - Mantém histórico de pagamentos
   - Permite consultas por período
   - Facilita cálculos e relatórios

## 7. Benefícios da Normalização

1. **Integridade dos Dados:**
   - Sem redundância de informações
   - Dados consistentes
   - Relacionamentos bem definidos

2. **Facilidade de Manutenção:**
   - Atualização simples de dados pessoais
   - Gestão eficiente de faltas
   - Controle preciso de pagamentos

3. **Flexibilidade:**
   - Fácil adição de novos tipos de informação
   - Suporte a múltiplos registros bancários
   - Histórico completo de faltas

4. **Consultas Eficientes:**
   - Relatórios por período
   - Análise de frequência
   - Folha de pagamento automatizada
