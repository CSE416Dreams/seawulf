from src.GerrymanderingMCMC import GerrymanderingMCMC
import sys

default_file = "./src/data/iowa.json"

def main():
    '''
    parser = argparse.ArgumentParser(description='Use MCMC Simulation to generate districting plans and plot relevant key statistics to illustrate the possibility that a source plan was gerrymandered')
    parser.add_argument("-g", "--graph_file", default=default_file, help="A path to a potential districting plan specified in this projects proprietary json schema; defaults to ./src/data/iowa.json")
    parser.add_argument("-c", "--cooling_period", type=int, default=50, help="The number of plans you'd like to generate _before_ counting them towards your ensemble; defaults to 50")
    parser.add_argument("-r", "--rounds", type=int, default=200, help="The number of plans you'd like to generate and include in your ensemble; defaults to 200")
    parser.add_argument("-v", "--verbose", action="store_true", help="Include this flag if you'd like real-time output to the console")
    parser.add_argument("-s", "--state", type=int, default=4, help="The State for the given plan")
    args = parser.parse_args()
    '''
    graph_file = ''
    cooling_period = 50
    rounds = 250
    state = sys.argv[1]

    # Build the gerrymandering MCMC using the variables you've been provided
    mcmc = GerrymanderingMCMC(sys.argv[2], state, graph_file, cooling_period=cooling_period, rounds=rounds)
    # Generate alternative plans
    mcmc.generate_alternative_plans(rounds)

    # Save the data
if __name__ == "__main__":
    main()

