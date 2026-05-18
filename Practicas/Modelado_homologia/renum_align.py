# Script de PyMOL para renumerar y alinear los modelos generados por homología con el modelo de AlphaFold
# Uso: ejecutar run renum_align.py en la consola de PyMOL

# Cargar el modelo base
load TRIM24_AlphaFold.pdb, ref

# --- RING ---
load RING.pdb, ring
alter ring, resi=str(int(resi)+54)  # Renumerar (+54)
sort ring
align ring, ref
save RING_renum_aligned.pdb, ring
delete ring

# --- B-box 1 ---
load BBox1.pdb, bb1
alter bb1, resi=str(int(resi)+159)  # Renumerar (+159)
sort bb1
align bb1, ref
save BBox1_renum_aligned.pdb, bb1
delete bb1

# --- B-box 2 ---
load BBox2.pdb, bb2
alter bb2, resi=str(int(resi)+216)  # Renumerar (+216)
sort bb2
align bb2, ref
save BBox2_renum_aligned.pdb, bb2
delete bb2

# --- Coiled-coil ---
load CC.pdb, cc
alter cc, resi=str(int(resi)+265)  # Renumerar (+265)
sort cc
align cc, ref
save CC_renum_aligned.pdb, cc
delete cc

# --- 3O33 ---
load 3O33.cif, 3O33
align 3O33, ref
save 3O33_aligned.pdb, 3O33
delete 3O33
