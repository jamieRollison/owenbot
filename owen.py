# the owen object with its functions go here. if you are writing a description, please provide a description

import random
class Owen:
    sillies_list = "placeholder"

    #initalizes the files
    def __init__(self):
        with open('./resources/sillies.txt', 'r') as funny_file:
            self.sillies_list = funny_file.readlines()

    # returns the string "the __ store" for the death grips bit
    # precon: all the words exist in the string
    # doesn't work if the "store" joke contains the word store
    # also only finds the first one
    def capture_store_string(self, line):
        return line[line.find("the") : line.find("store") + 5]

    # pulls owenisms from the file and returns a random one
    def say_something_silly(self):
        return self.sillies_list[random.randint(0,len(self.sillies_list)-1)].strip()
    #does the
    def knower(self, line):
        for word in line.split(' '):
            if word.endswith('er'):
                return word