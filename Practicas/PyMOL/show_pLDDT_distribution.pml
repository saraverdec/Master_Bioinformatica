# Script de PyMOL para representar la distribución de pLDDT al estilo AlphaFold
# Uso: ejecutar run show_pLDDT_distribution.pml en la consola de PyMOL tras cargar el modelo

hide everything 
show cartoon 
bg_color white 

spectrum b, orange yellow cyan blue, minimum=50, maximum=90 

ray
# png alphafold.png, dpi=300