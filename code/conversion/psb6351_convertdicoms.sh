#!/bin/bash

#SBATCH -J psb6351_dcm_convert
#SBATCH -o /scratch/classroom/psb6351/amattfel/crash/dcm_convert_out
#SBATCH -e /scratch/classroom/psb6351/amattfel/crash/dcm_convert_err
#SBATCH --qos pq_psb6351
#SBATCH --account acc_psb6351
#SBATCH --partition classroom

heudiconv -d '/home/amattfel/Mattfeld_PSB6351/sourcedata/Mattfeld_REVL-000-vCAT-{subject}-S1/*/*/*/*/*/*' -s 021 -c none -f convertall -o /home/amattfel/Mattfeld_PSB6351/dset

