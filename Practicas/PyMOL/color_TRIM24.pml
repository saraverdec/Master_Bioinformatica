# Script de PyMOL para colorear los diferentes dominios de TRIM24
# Uso: ejecutar run color_TRIM24.pml en la consola de PyMOL
load TRIM24_min.pdb, TRIM24
hide everything
show cartoon, TRIM24

# Colorear cada dominio
color cyan, resi 56-82        # RING
color magenta, resi 158-211   # B-box 1
color magenta, resi 218-259   # B-box 2
color yellow, resi 260-392    # Coiled-coil
color salmon, resi 826-873    # PHD
color purple, resi 899-1006   # Bromodominio

# Mostrar los iones de zinc como esferas
show spheres, resn ZN
color gray, resn ZN
set sphere_scale, 0.5

# Fondo blanco para mejor contraste
bg_color white

ray
# png alphafold.png, dpi=300