# Lab 10 – TDD: testes + respostas

Conteúdo:
- exN/tests/  → os testes finais de cada exercício (a lista pronta)
- exN/pyproject.toml → configuração do slide 4
- respostas.md → respostas das letras a) a e), sem código de produção

O código de produção (src/) não está incluído de propósito: escreva-o você,
um teste por vez, seguindo os ciclos de respostas.md. Cada pasta já tem
pyproject.toml; crie exN/src/ com o módulo (contador.py, fila.py, carrinho.py).

Como usar (Codespaces):
    pip install pytest==9.1.1 pytest-cov==7.1.0 mutmut==3.8.0
    cd ex1 && pytest -q --cov=src --cov-branch
    mutmut run && mutmut results

Dica: para praticar RED de verdade, copie o arquivo de testes e vá liberando
um teste por vez (comente os demais). Ex3: parta do carrinho da teoria
(slides 15 e 16) – com os testes novos, vários falham de início, que é o RED.
