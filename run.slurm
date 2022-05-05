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

#parallel --jobs 40 "python cli.py --state fl"
#parallel --jobs 40 "python cli.py --state ms"
#parallel --jobs 40 "python cli.py --state ga"

parallel --jobs 40 python3 "cli.py fl" {} ::: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
parallel --jobs 40 python3 "cli.py ms" {} ::: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
parallel --jobs 40 python3 "cli.py ga" {} ::: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
