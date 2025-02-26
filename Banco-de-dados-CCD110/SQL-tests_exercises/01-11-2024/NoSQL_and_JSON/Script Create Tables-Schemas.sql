CREATE SCHEMA jsonsql

-- Criando a tabela produtos com uma coluna JSONB
CREATE TABLE jsonsql.produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    detalhes JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserindo dados com diferentes estruturas JSON
INSERT INTO jsonsql.produtos (nome, detalhes) VALUES
(
    'Smartphone Galaxy S21',
    '{
        "especificacoes": {
            "tela": "6.2 polegadas",
            "processador": "Exynos 2100",
            "ram": "8GB",
            "armazenamento": "256GB"
        },
        "cores_disponiveis": ["preto", "branco", "roxo"],
        "garantia_meses": 12,
        "acessorios_inclusos": ["carregador", "fone", "capa"]
    }'
),
(
    'Notebook Dell XPS',
    '{
        "especificacoes": {
            "processador": "Intel i7",
            "ram": "16GB",
            "ssd": "512GB",
            "tela": "15.6 polegadas 4K"
        },
        "cores_disponiveis": ["prata", "preto"],
        "garantia_meses": 24,
        "sistema_operacional": "Windows 11"
    }'
),
(
    'Smart TV LG',
    '{
        "especificacoes": {
            "tamanho": "55 polegadas",
            "resolucao": "4K",
            "taxa_atualizacao": "120Hz"
        },
        "recursos": ["HDR", "Wifi", "Bluetooth"],
        "apps_instalados": ["Netflix", "Prime Video", "Disney+"],
        "garantia_meses": 12
    }'
);