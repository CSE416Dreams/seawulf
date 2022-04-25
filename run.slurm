#!/usr/bin/env bash

#SBATCH --job-name=generate_plans
#SBATCH --ntasks-per-node=<cores for each node>
#SBATCH --nodes=<amount of nodes>
#SBATCH --time=<time as specified by the reqs>
#SBATCH -p <name of queue>
#SBATCH --output=<file for logs>

module load anaconda/3
module load openmpi/4.0.5

mpirun -np <process across all nodes> python cli.py -c 50 -g <graph file> -r 10000 -n <numm of districts>
