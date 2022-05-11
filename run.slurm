#!/usr/bin/env bash

#SBATCH --job-name=generate_plans
#SBATCH --ntasks-per-node=40
#SBATCH --nodes=1
#SBATCH --time=30:00:00
#SBATCH -p long-40core
#SBATCH --output=<file for logs>

module load anaconda/3
module load gnu-parallel/6.0
source activate sea

parallel --jobs 40 python3 "runner.py fl" {} ::: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
parallel --jobs 40 python3 "runner.py ms" {} ::: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
parallel --jobs 40 python3 "runner.py ga" {} ::: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
