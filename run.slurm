#!/usr/bin/env bash

#SBATCH --job-name=generate_plans
#SBATCH --ntasks-per-node=40
#SBATCH --nodes=1
#SBATCH --time=<time as specified by the reqs>
#SBATCH -p <name of queue>
#SBATCH --output=<file for logs>

module load anaconda/3
module load gnu-parallel/6.0
conda activate

parallel --jobs 40 "python cli.py --state fl"
parallel --jobs 40 "python cli.py --state ms"
parallel --jobs 40 "python cli.py --state ga"
