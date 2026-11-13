#!/usr/bin/env bash
# Re-executa TODAS as etapas de TODOS os exercicios do zero e regenera os logs.
# Uso:  bash rodar_tudo.sh      (precisa de: pip install pytest==9.1.1 pytest-cov==7.1.0 mutmut==3.8.0)
cd "$(dirname "$0")"
rm -f ex*/logs/a_* ex*/logs/b_* ex*/logs/c_* ex*/logs/d_*

run() { ./rodar_etapa.sh "$1" "$2" >/dev/null 2>&1; ./mostrar_mutantes.sh "$1" "$2" todos >/dev/null 2>&1
        printf "%-4s %-10s %s\n" "$1" "$2" "$(cat $1/logs/${2}_4_resumo.txt)"; }

run ex1 a_inicial; run ex1 d_match; run ex1 e_match_ancorado; run ex1 c_final
run ex2 a_inicial; run ex2 b_exato; run ex2 d_final
run ex3 a_inicial; run ex3 c_final
run ex4 a_bva;     run ex4 c_final

# deixa em tests/ a suite FINAL de cada exercicio e limpa arquivos temporarios
for par in "ex1 c_final" "ex2 d_final" "ex3 c_final" "ex4 c_final"; do
  set -- $par; rm -rf $1/tests/* $1/mutants; cp $1/etapas/$2/*.py $1/tests/
done
find . -name __pycache__ -type d -prune -exec rm -rf {} + ; rm -rf ex*/.coverage ex*/.pytest_cache ex*/mutants
