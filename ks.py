from argparse import ArgumentParser
from Greedy import *
from Memoization import *
from Tabulation import *
import DataReader as dr
from Utilities import *
import time
from datetime import datetime



def args_creator():
    parser = ArgumentParser()

    parser.add_argument("-d", "--directory", action="store", dest="directory", default="", help="directory (process many files)", metavar="[DIRECTORY]")
    parser.add_argument("-f", "--file", action="store", dest="file", default="", help="file (process a single file)", metavar="[FILE]")

    parser.add_argument("-b", "--benefit", action="store_true", dest="showBenefit", default=False, help="Display benefit")
    parser.add_argument("-r", "--room", action="store_true", dest="showRoom", default=False, help="Display room (unused knapsack weight)")

    parser.add_argument("-t", "--time", action="store_true", dest="timer", default=False, help="Display time")

    parser.add_argument("-dt", "--display_taken", action="store_true", dest="showTaken", default=False, help="Display identifier of taken items")

    parser.add_argument("-sg", "--greedy", action="store_true", dest="greedy", default=False, help="Solve it with Greedy")
    parser.add_argument("-sm", "--memoization", action="store_true", dest="memoization", default=False, help="Solve it with Memoization")
    parser.add_argument("-st", "--tabulation", action="store_true", dest="tabulation", default=False, help="Solve it with Tabulation")

    return parser.parse_args()


if __name__ == '__main__':
    args = args_creator()
    items = None
    capacity = 0
    if args.directory != "":
        items, capacity = dr.readFile(dr.readAllFiles(args.directory))
    elif args.file != "":
        items, capacity = dr.readFile(args.file)
    else:
        print("Introduzca un fichero, por favor")
        exit(-1)

    if len(items) <= 0:
        print("Error en la lectura del archivo")
        exit(-1)

    t0 = 0
    t1 = 0
    if args.greedy:
        print("Solving it with Greedy")
        t0 = time.time()
        value, taken = solve_greedy(items, capacity)
        t1 = time.time()
    elif args.memoization:
        print("Solving it with Memoization")
        t0 = time.time()
        value, taken = memoization(items, capacity)
        t1 = time.time()
    elif args.tabulation:
        print("Solving it with Tabulation")
        t0 = time.time()
        value, taken = tabulation(items, capacity)
        t1 = time.time()
    else:
        print("Introduzca un metodo, por favor")
        exit(-1)

    if args.showBenefit:
        print("Benefit =", get_total_value(items, taken))
    if args.showRoom:
        print("Room =", get_left_weight(capacity, items, taken))
    if args.showTaken:
        print("Take items =", taken_items(items, taken))
    if args.timer:
        t = (t1 - t0)
        print("Time =", round(t, 3), "s")
