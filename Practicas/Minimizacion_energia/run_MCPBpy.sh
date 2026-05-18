for f in ZN{1..7}.in; do
    base=${f%.in}

    echo ">>> Procesando $base"

    MCPB.py -i "$f" -s 1a # Preparar los archivos necesarios
    MCPB.py -i "$f" -s 2e # Generar archivo FRCMOD sin hacer cálculos con Gaussian
    MCPB.py -i "$f" -s 4b # Generar archivo de entrada para LEaP correspondiente al modelo enlazado

    echo ">>> Terminado $base"
    echo
done
