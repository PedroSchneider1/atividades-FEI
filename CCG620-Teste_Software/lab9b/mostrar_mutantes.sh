#!/usr/bin/env bash
# Uso: ./mostrar_mutantes.sh ex1 a_inicial [todos|vivos]
# Grava o diff (mutmut show) de cada mutante em exN/logs/<etapa>_5_diffs.txt
EX="$1"; ETAPA="$2"; MODO="${3:-todos}"
cd "$(dirname "$0")/$EX" || exit 1
OUT="logs/${ETAPA}_5_diffs.txt"
: > "$OUT"
if [ "$MODO" = "vivos" ]; then
  LISTA=$(mutmut results 2>&1 | grep ': ' | awk -F: '{print $1}' | tr -d ' ')
else
  LISTA=$(mutmut results --all true 2>&1 | grep ': ' | awk -F: '{print $1}' | tr -d ' ')
fi
for m in $LISTA; do
  ST=$(mutmut results --all true 2>&1 | grep -F "$m:" | awk -F': ' '{print $2}')
  echo "=================== $m  [$ST]" >> "$OUT"
  mutmut show "$m" 2>&1 | grep -E '^[-+@]' | grep -vE '^(---|\+\+\+)' >> "$OUT"
done
cat "$OUT"
