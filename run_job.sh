#!/bin/bash

export HOME="/home/iibarra"
export USER="iibarra"
export PATH="/home/mlrsrv/anaconda3/bin:/usr/bin:/bin"
# export HTTP_PROXY="http://mlrsrv:OaMv10QQ@10.1.1.96:3128"
# export HTTPS_PROXY="http://mlrsrv:OaMv10QQ@10.1.1.96:3128"
# export UV_PYTHON="/home/mlrsrv/anaconda3/bin/python"
# export UV_PYTHON_DOWNLOADS=never
# export UV_PYTHON_PREFERENCE=only-managed

# Configuracion
BASE_DIR="/home/iibarra/work/bora_wrapper"
LOG_DIR="$BASE_DIR/job_logs"
LOG_FILE="$LOG_DIR/bora_job_$(date +%Y%m%d).log"
CURRENT_DATE="$(date +%d/%m/%Y)"
RUBRO="CONSTITUCION SA"

echo "USER: $(whoami)" >> "$LOG_FILE"
echo "PATH: $PATH" >> "$LOG_FILE"
echo "PWD: $(pwd)" >> "$LOG_FILE"

# Asegurar directorio de logs
mkdir -p "$LOG_DIR"

# Ir al directorio del proyecto
cd "$BASE_DIR" || exit 1

# Marca de inicio
echo "===== START $(date '+%Y-%m-%d %H:%M:%S') =====" >> "$LOG_FILE"

# Ejecutar job
/home/iibarra/.local/bin/uv run bora-cli --start-date "$CURRENT_DATE" --end-date "$CURRENT_DATE" --rubro "$RUBRO" >> "$LOG_FILE" 2>&1

# Guardar codigo de salida
EXIT_CODE=$?

# Marca de fin
echo "===== END $(date '+%Y-%m-%d %H:%M:%S') | EXIT CODE: $EXIT_CODE =====" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

exit $EXIT_CODE