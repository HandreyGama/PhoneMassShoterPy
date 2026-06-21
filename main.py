import argparse
from src.controllers.cli import run
parser =  argparse.ArgumentParser(
    prog="* PhoneMassShoterPy *",
    description="A Simple program to Send Messages for numbers registered in" \
    "supabase",
    epilog="For more info see: {github link}"
    )

parser.add_argument("-t",'--type')
parser.add_argument("-m",'--message')
parser.add_argument("-r",'--rate_limit')


args = parser.parse_args()

if __name__ == "__main__":
    if args.type == "script":
        run(args)
        pass
    elif args.type == "server":
        print("This feature is not implemented yet!")
        pass