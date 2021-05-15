#!/bin/bash

#SBATCH --partition=batch
#SBATCH --qos=240c-9d_batch
#SBATCH --nodes=1
#SBATCH --ntasks=20
#SBATCH --mem=50GB
#SBATCH --job-name="DOS"
#SBATCH --output=DOS.%J.out
#SBATCH --error=DOS.%J.err
#SBATCH --exclude=saliksik-cpu-[01]


echo "SLURM_JOBID="$SLURM_JOBID
echo "SLURM_JOB_NODELIST"=$SLURM_JOB_NODELIST
echo "SLURM_NNODES"=$SLURM_NNODES
echo "SLURMTMPDIR="$SLURMTMPDIR
echo "working directory = "$SLURM_SUBMIT_DIR

# export downloaded apps
. /home/melsa.ducut/apps/oneapi/setvars.sh
export PATH=$PATH:/home/melsa.ducut/apps/qe-6.7/bin
# Set stack size to unlimited
export OMP_NUM_THREADS=1
ulimit -s unlimited

# run Quantum Espresso using Open MPI's mpirun
#mpirun -np 10 pw.x -nk 2 -in mos2_0_relax.in > mos2_0_relax.out
#mpirun -np 10 pw.x -in mos2_1_scf.in > mos2_1_scf.out
#mpirun -np 10 pw.x -in mos2_2_nscf.in > mos2_2_nscf.out
#cd ~/final_calculations_MoS2
#mkdir BENCHMARK_MOS2_PBE_FINAL
#cd BENCHMARK_MOS2_PBE_FINAL
#mkdir MoS2_1x1_DOS
#mkdir MoS2_1x1_BAND
#cd ~/scratch1/NEW_QE_CALC/BENCHMARK_MOS2_PBE_FINAL/
#mkdir MoS2_1x1_DOS
#cd ~/scratch1/NEW_QE_CALC/BENCHMARK_MOS2_PBE_FINAL/MoS2_1x1_BAND
#cp -r . ~/scratch1/NEW_QE_CALC/BENCHMARK_MOS2_PBE_FINAL/MoS2_1x1_DOS
mpirun -np 10 pw.x -in mos2_3_pwbands.in > mos2_3_pwbands.out
mpirun -np 10 bands.x -in mos2_4_bands.in > mos2_4_bands.out
mpirun -np 10 plotband.x < mos2_5_plotband.in > mos2_5_plotband.out
#cp -r . /home/melsa.ducut/final_calculations_MoS2/BENCHMARK_MOS2_PBE_FINAL/MoS2_1x1_BAND

#mpirun -np 10 dos.x -in mos2_6_dos.in > mos2_6_dos.out
#cp -r . /home/melsa.ducut/final_calculations_MoS2/BENCHMARK_MOS2_PBE_FINAL/MoS2_1x1_DOS
