# Normalização do Esquema de Consultas Médicas

## 1. Análise da Estrutura Original

### Tabelas Originais:
```
Médico(CRM, med-nome, med-telefone, {med_data_consulta, med-hora_consulta, codigo_paciente})

Paciente(pac_codigo, pac_nome, pac_ddd, pac_telefone, {cod_convenio, descricao_convenio})

Consulta(CRM-Medico, codigo_paciente, data_consulta, hora-consulta, valor_consulta, cod_convenio, descricao_convenio)
```

### Identificação dos Atributos

#### Médico:
- CRM (identificador do médico)
- med-nome
- med-telefone
- Grupo repetitivo de consultas:
  - med_data_consulta [multivalorado]
  - med-hora_consulta [multivalorado]
  - codigo_paciente [multivalorado]

#### Paciente:
- pac_codigo (identificador do paciente)
- pac_nome
- pac_ddd
- pac_telefone
- Grupo repetitivo de convênios:
  - cod_convenio [multivalorado]
  - descricao_convenio [multivalorado]

#### Consulta:
- CRM-Medico
- codigo_paciente
- data_consulta
- hora-consulta
- valor_consulta
- cod_convenio
- descricao_convenio

## 2. Identificação das Dependências Funcionais

### DFs na tabela Médico:
1. `CRM → med-nome, med-telefone`
   - O CRM determina o nome e telefone do médico

### DFs na tabela Paciente:
1. `pac_codigo → pac_nome, pac_ddd, pac_telefone`
   - O código do paciente determina seus dados pessoais

### DFs na tabela Consulta:
1. `(CRM-Medico, data_consulta, hora-consulta) → codigo_paciente, valor_consulta`
   - A combinação de médico, data e hora determina o paciente e valor

2. `cod_convenio → descricao_convenio`
   - O código do convênio determina sua descrição

### DFs adicionais:
1. `(CRM-Medico, data_consulta, hora-consulta) → codigo_paciente`
   - Não pode haver duas consultas no mesmo horário para o mesmo médico

## 3. Processo de Normalização

### 1ª Forma Normal (1FN)
- Eliminar grupos repetitivos
- Criar tabelas separadas para atributos multivalorados

### 2ª e 3ª Formas Normais (2FN e 3FN)
- Remover dependências parciais e transitivas
- Criar tabelas separadas para cada entidade

## 4. Esquema Final Normalizado

```sql
-- Tabela de Médicos
CREATE TABLE MEDICO (
    CRM VARCHAR(20) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20)
);

-- Tabela de Pacientes
CREATE TABLE PACIENTE (
    codigo INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    ddd VARCHAR(3),
    telefone VARCHAR(20)
);

-- Tabela de Convênios
CREATE TABLE CONVENIO (
    codigo INT PRIMARY KEY,
    descricao VARCHAR(100) NOT NULL
);

-- Tabela de Pacientes e seus Convênios
CREATE TABLE PACIENTE_CONVENIO (
    codigo_paciente INT,
    codigo_convenio INT,
    CONSTRAINT pk_pac_conv PRIMARY KEY (codigo_paciente, codigo_convenio),
    CONSTRAINT fk_paciente FOREIGN KEY (codigo_paciente) 
        REFERENCES PACIENTE(codigo),
    CONSTRAINT fk_convenio FOREIGN KEY (codigo_convenio) 
        REFERENCES CONVENIO(codigo)
);

-- Tabela de Consultas
CREATE TABLE CONSULTA (
    CRM_medico VARCHAR(20),
    data_consulta DATE,
    hora_consulta TIME,
    codigo_paciente INT NOT NULL,
    valor_consulta DECIMAL(10,2) NOT NULL,
    codigo_convenio INT,
    CONSTRAINT pk_consulta PRIMARY KEY (CRM_medico, data_consulta, hora_consulta),
    CONSTRAINT fk_medico FOREIGN KEY (CRM_medico) 
        REFERENCES MEDICO(CRM),
    CONSTRAINT fk_paciente_consulta FOREIGN KEY (codigo_paciente) 
        REFERENCES PACIENTE(codigo),
    CONSTRAINT fk_convenio_consulta FOREIGN KEY (codigo_convenio) 
        REFERENCES CONVENIO(codigo)
);

-- Índices para otimização
CREATE INDEX idx_consulta_paciente ON CONSULTA(codigo_paciente);
CREATE INDEX idx_consulta_data ON CONSULTA(data_consulta);
CREATE INDEX idx_paciente_nome ON PACIENTE(nome);
CREATE INDEX idx_medico_nome ON MEDICO(nome);
```

## 5. Views Úteis

```sql
-- View para agenda do médico
CREATE VIEW AGENDA_MEDICO AS
SELECT 
    m.CRM,
    m.nome as nome_medico,
    c.data_consulta,
    c.hora_consulta,
    p.nome as nome_paciente,
    cv.descricao as convenio,
    c.valor_consulta
FROM MEDICO m
JOIN CONSULTA c ON m.CRM = c.CRM_medico
JOIN PACIENTE p ON c.codigo_paciente = p.codigo
LEFT JOIN CONVENIO cv ON c.codigo_convenio = cv.codigo;

-- View para histórico de consultas do paciente
CREATE VIEW HISTORICO_PACIENTE AS
SELECT 
    p.codigo as codigo_paciente,
    p.nome as nome_paciente,
    m.nome as nome_medico,
    c.data_consulta,
    c.hora_consulta,
    cv.descricao as convenio,
    c.valor_consulta
FROM PACIENTE p
JOIN CONSULTA c ON p.codigo = c.codigo_paciente
JOIN MEDICO m ON c.CRM_medico = m.CRM
LEFT JOIN CONVENIO cv ON c.codigo_convenio = cv.codigo
ORDER BY c.data_consulta DESC, c.hora_consulta DESC;
```

## 6. Benefícios da Normalização

1. **Integridade dos Dados:**
   - Cada médico tem um CRM único
   - Não há conflitos de horários para consultas
   - Dados de convênios consistentes

2. **Eliminação de Redundância:**
   - Dados do médico armazenados uma única vez
   - Dados do paciente centralizados
   - Informações de convênio não duplicadas

3. **Facilidade de Manutenção:**
   - Atualização de dados do médico em um lugar
   - Gestão de convênios simplificada
   - Histórico de consultas organizado

4. **Consultas Eficientes:**
   - Fácil busca por período
   - Relatórios por médico ou paciente
   - Controle financeiro simplificado

## 7. Melhorias em Relação ao Esquema Original

1. **Estrutura:**
   - Separação clara entre entidades
   - Relacionamentos bem definidos
   - Eliminação de grupos repetitivos

2. **Dados:**
   - Não há duplicação de informações
   - Consistência garantida
   - Fácil manutenção

3. **Performance:**
   - Índices adequados
   - Views para consultas comuns
   - Melhor utilização do espaço
