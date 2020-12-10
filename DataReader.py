from Utilities import *
import os


def readAllFiles(path):
    files = os.listdir(path)
    items = []
    for f in files:
        items.append(readDataFile(f))

    return items


def readFile(file):
    f = open(file, "r")
    content = f.read().split('\n')
    first_line = content[0].split()
    item_count = int(first_line[0])
    capacity = int(first_line[1])

    items = []
    for i in range(1, item_count + 1):
        line = content[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    return items, capacity


def readDataFile(name):
    f = open("input-files/" + name, "r")
    content = f.read().split('\n')
    first_line = content[0].split()
    item_count = int(first_line[0])
    capacity = int(first_line[1])

    items = []
    for i in range(1, item_count + 1):
        line = content[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    return items, capacity
