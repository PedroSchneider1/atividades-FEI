#!/usr/bin/env bash
# Roda as suites (BVA e final) contra o mutante de 2a ordem feito a mao.
# Uso (a partir da raiz do lab):  bash ex4/extras/rodar_mutante_2a_ordem.sh
RAIZ="$(cd "$(dirname "$0")/../.." && pwd)"
TMP=$(mktemp -d)
for ETAPA in a_bva c_final; do
  rm -rf "$TMP"/*; mkdir -p "$TMP/tests"
  cp "$RAIZ/ex4/extras/mutante_2a_ordem/multa.py" "$TMP/multa.py"
  cp "$RAIZ/ex4/etapas/$ETAPA/test_multa.py" "$TMP/tests/"
  echo "=== suite $ETAPA contra o mutante de 2a ordem ==="
  (cd "$TMP" && PYTHONPATH="$TMP" python3 -m pytest -q -p no:cacheprovider tests 2>&1 | grep -E "FAILED|passed|failed")
  echo
done
rm -rf "$TMP"
