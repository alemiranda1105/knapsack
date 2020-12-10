from argparse import ArgumentParser
from Greedy import *
from DataReader import *
from Utilities import *


def start():
    items, capacity = readDataFile("data_4")
    value, taken = solve_greedy(items, capacity)

    print(check_solution(capacity, items, taken), end='')
    print(taken_items(items, taken))


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
    print(args.directory)
    if args.timer:
        print("timer")
    else:
        print("casi")


