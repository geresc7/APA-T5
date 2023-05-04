#! /usr/bin/python3

if __name__ == "__main__":
    from docopt import docopt
    import sys
    
    usage = """
            naval_fate ship new <name>...
            naval_fate ship <name> move <x> <y> [--speed=<kn>]
            naval_fate ship shoot <x> <y>
            naval_fate mine (set|remove) <x> <y> [--moored|--drifting]
            naval_fate -h | --help
            naval_fate --version  
            Options:
            -h --help     Show this screen.
            --version     Show version.
            --speed=<kn>  Speed in knots [default: 10].
            --moored      Moored (anchored) mine.
            --drifting    Drifting mine. 
    """

    args = docopt(usage, sys.argv, help=True, version="Y a su barco le llamó Libertad", options_first=False)

    print(args["<name>"])