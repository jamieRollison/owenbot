# misc functions go here. if you are writing them, please provide a description

import random

# returns the string "the __ store" for the death grips bit
# precon: all the words exist in the string
# doesn't work if the "store" joke contains the word store
# also only finds the first one
def capture_store_string(line):
    return line[line.find("the") : line.find("store") + 5]

# pulls owenisms from the file and returns a random one
def say_something_silly():
    with open('./resources/sillies.txt', 'r') as funny_file:
        lines = funny_file.readlines()
        return lines[random.randint(0,len(lines)-1)].strip()

