#!/bin/bash

export HOME="/home/iibarra"
export USER="iibarra"
export PATH="/home/mlrsrv/anaconda3/bin:/usr/bin:/bin"

# Configuracion
BASE_DIR="/home/iibarra/work/bora_wrapper"
LOG_DIR="$BASE_DIR/job_logs"
LOG_FILE="$LOG_DIR/bora_job_$(date +%Y%m%d).log"
CURRENT_DATE="$(date +%d/%m/%Y)"

# Asegurar directorio de logs
mkdir -p "$LOG_DIR"

echo "USER: $(whoami)" >> "$LOG_FILE"
echo "PATH: $PATH" >> "$LOG_FILE"
echo "PWD: $(pwd)" >> "$LOG_FILE"

# Ir al directorio del proyecto
cd "$BASE_DIR" || exit 1

# Marca de inicio
echo "===== START $(date '+%Y-%m-%d %H:%M:%S') =====" >> "$LOG_FILE"

# Ejecutar job
/home/iibarra/.local/bin/uv run bora-cli --start-date "$CURRENT_DATE" --end-date "$CURRENT_DATE" --rubros "CONSTITUCION SA" >> "$LOG_FILE" 2>&1

sleep 5

/home/iibarra/.local/bin/uv run bora-cli --start-date "$CURRENT_DATE" --end-date "$CURRENT_DATE" --rubros "CONTRATO SRL" >> "$LOG_FILE" 2>&1

sleep 5

/home/iibarra/.local/bin/uv run bora-cli --start-date "$CURRENT_DATE" --end-date "$CURRENT_DATE" --rubros "CONSTITUCION SAS" >> "$LOG_FILE" 2>&1

# Guardar codigo de salida
EXIT_CODE=$?

# Marca de fin
echo "===== END $(date '+%Y-%m-%d %H:%M:%S') | EXIT CODE: $EXIT_CODE =====" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

exit $EXIT_CODE
