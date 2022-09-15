#!/bin/bash

#SBATCH -J psb6351_dcm_convert
#SBATCH -o /scratch/madlab/Mattfeld_PSB6351/crash/dcm_convert_out
#SBATCH -e /scratch/madlab/Mattfeld_PSB6351/crash/dcm_convert_err
#SBATCH --qos pq_madlab
#SBATCH --account iacc_madlab
#SBATCH --partition IB_40C_512G

heudiconv -d '/home/amattfel/Mattfeld_PSB6351/sourcedata/Mattfeld_REVL-000-vCAT-{subject}-S1/*/*/*/*/*/*' -s 021 -c none -f convertall -o /home/amattfel/Mattfeld_PSB6351/dset

