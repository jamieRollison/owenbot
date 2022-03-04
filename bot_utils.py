# misc functions go here. if you are writing them, please provide a description

# returns the string "the __ store" for the death grips bit
# precon: all the words exist in the string
def capture_store_string(line):
    return line[line.find("the") : line.find("store") + 5]