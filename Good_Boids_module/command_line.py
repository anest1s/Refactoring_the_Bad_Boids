import sys
from argparse import ArgumentParser
from Good_Boids_module.Animate_Boids import Animator


def process():
    parser = ArgumentParser(description="Simulation of boids' flocking")
    
    # Parameters
    parser.add_argument('--file', dest='configuration_file',  help="Choose your configuration file")

    # Print help message even if no flag is provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    argument = parser.parse_args()

    # Exceptions if file does not exist
    try:
        animate = Animator(argument.configuration_file)
        animate.figure()

    except IOError:
        print("THIS FILE DOES NOT EXIST.\n")
        parser.print_help()
    except:
        print("Unexpected error.", sys.exc_info()[0], "\n")
        raise

if __name__ == "__main__":
    process()