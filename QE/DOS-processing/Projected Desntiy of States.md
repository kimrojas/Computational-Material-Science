```
#!/bin/bash
#SBATCH --partition=batch
#SBATCH --qos=240c-1h_batch
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --mem=64G
#SBATCH --exclude=saliksik-cpu-[01]
# - - - - - - - - - - - - - - - - - - - -
NP=4
source ~/.bash_profile
. /home/kurt.rojas/APPS/intel/oneapi/setvars.sh
export PATH=$PATH:/home/kurt.rojas/APPS/qe-6.7/bin/
export OMP_NUM_THREADS=1
ulimit -s unlimited
# - - - - - - - - - - - - - - - - - - - -
# For Issues, see: http://www.ehu.eus/sgi/ARCHIVOS/espresso

# SETTINGS
KEYWORD="dos"
INPUT="in.$KEYWORD"
OUTPUT="out.$KEYWORD"
rm -rf *$KEYWORD

cat << EOF > $INPUT
 &PROJWFC
    prefix='base',
    outdir='../nscf/tmp',
    filpdos='base',
    filproj='base.filproj'
    Emin=-20.0, Emax=20.0,
    degauss=0.005,

 /
EOF

########################################
mpirun -np $NP projwfc.x -in $INPUT > $OUTPUT
```