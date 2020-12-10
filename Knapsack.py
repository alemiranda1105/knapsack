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
    parser.add_argument("-d", "--directory", help="directory (process many files)", metavar="[DIRECTORY]")
    parser.add_argument("-f", "--file", help="file (process a single file)", metavar="[FILE]")
    parser.add_argument("-b", "--benefit", help="Display benefit")
    parser.add_argument("-r", "--room", help="Display room (unused knapsack weight)")
    parser.add_argument("-t", "--time", help="Display time")
    parser.add_argument("-dt", "--display_taken", help="Display identifier of taken items")
    parser.add_argument("-sg", "--greedy", nargs='?', help="Solve it with Greedy")
    parser.add_argument("-sm", "--memoization", nargs='?', help="Solve it with Memoization")
    parser.add_argument("-st", "--tabulation", nargs='?', help="Solve it with Tabulation")

    parser.parse_args()


if __name__ == '__main__':
    start()


