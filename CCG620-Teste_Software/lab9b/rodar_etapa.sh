#!/usr/bin/env bash
# Uso: ./rodar_etapa.sh ex1 a_inicial
# Copia os testes de exN/etapas/<etapa>/ para exN/tests/, mede cobertura,
# roda o mutmut e grava tudo em exN/logs/<etapa>_*.txt
set -u
EX="$1"; ETAPA="$2"
RAIZ="$(cd "$(dirname "$0")" && pwd)"
cd "$RAIZ/$EX" || exit 1

rm -rf tests/* mutants .coverage .pytest_cache
cp etapas/"$ETAPA"/*.py tests/

LOG="logs/${ETAPA}"
echo "### pytest + cobertura de ramos ($EX / $ETAPA)" | tee "${LOG}_1_cobertura.txt"
pytest -q --cov=src --cov-branch --cov-report=term-missing 2>&1 | tee -a "${LOG}_1_cobertura.txt"

echo "### mutmut run ($EX / $ETAPA)" | tee "${LOG}_2_mutmut_run.txt"
mutmut run 2>&1 | tr '\r' '\n' | tail -5 | tee -a "${LOG}_2_mutmut_run.txt"

echo "### mutmut results --all true" | tee "${LOG}_3_resultados.txt"
mutmut results --all true 2>&1 | tee -a "${LOG}_3_resultados.txt"

# resumo numerico
TOTAL=$(mutmut results --all true 2>&1 | grep -c ': ')
MORTOS=$(mutmut results --all true 2>&1 | grep -c ': killed')
VIVOS=$(mutmut results --all true 2>&1 | grep -c ': survived')
echo "RESUMO: gerados=$TOTAL mortos=$MORTOS vivos=$VIVOS" | tee "${LOG}_4_resumo.txt"
