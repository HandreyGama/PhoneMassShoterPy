import argparse

parser =  argparse.ArgumentParser(
    prog="* PhoneMassShoterPy *",
    description="A Simple program to Send Messages for numbers registered in" \
    "supabase",
    epilog="For more info see: {github link}"
    )

parser.add_argument("-t",'--type')
parser.add_argument("-m",'--message')

args = parser.parse_args()

if __name__ == "__main__":
    if args.type == "script":
        pass
    elif args.type == "server":
        pass