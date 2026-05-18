from modeller import *
from modeller.automodel import *

log.verbose()
env = Environ()
env.io.hetatm = True  # Para conservar los Zn en el modelo

a = AutoModel(env,
              alnfile='alignment.ali',
              knowns=('TRIM24', 'RING', 'BB1', 'BB2', 'CC', 'PHD_BROMODOMAIN'),
              sequence='TRIM24_chimera',
              assess_methods=(assess.DOPE, assess.GA341))

# --- Parámetros de refinamiento ---
a.library_schedule = autosched.slow
a.max_var_iterations = 300
a.md_level = refine.slow   # refine.very_slow para mayor refinamiento

# --- Número de modelos a generar ---
a.starting_model = 1
a.ending_model = 1

# --- Generación del modelo ---
a.make()