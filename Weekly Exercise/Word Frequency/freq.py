# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name = Jenish Patel
# Student ID: 1572027
# CMPUT 274, FALL 2019
# Weekly Assignment: Word Frequency
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import sys
import os.path


def openFile():
    '''Takes in the command line arguement entered by the user
    and opens the respective file. It removes newline characters
    and appends each line into a list. Additional it removes
    lines which have no characters which are indicated by an empty
    element in the list.'''
    fname = commandInput()
    inFile = open(fname, "r")

    raw_list = ['']
    for line in inFile:
        line = line.strip('\n')
        raw_list.append(line)

    while '' in raw_list:
        raw_list.remove('')

    sort_analysis(raw_list, fname)
    inFile.close()


def commandInput():
    '''This function assures that the user is typing valid
    commands in the terminal. It will indicate by printing
    out an error message if the user types in additonal or
    minimal file information.'''
    cmd_arg_list = []

    for i in sys.argv:
        cmd_arg_list.append(i)

    if len(cmd_arg_list) < 2:
        print('too few command line arguments')
        exit()
    elif len(cmd_arg_list) > 2:
        print('too many command line arguments')
        exit()

    fname = cmd_arg_list[1]

    if not(os.path.isfile(fname)):
        print('File does not exist')
        exit()

    return fname


def sort_analysis(raw_list, fname):
    '''Analyizes the raw_list passed by the openFile function
    and returns the occurances of each word and frequency of
    each word in the file.'''

    ''' Converts elements containing lines of words to each
    element containing a single word.'''
    raw_list = (' '.join(raw_list).split())
    # Sorts list in to lexicographic order
    raw_list.sort()

    # empty list to stores values of occurances
    values = []
    counter = 0

    ''' Transforms the pre-existing list by eliminating repeating
    words.'''
    lexico_order_list = list(dict.fromkeys(raw_list))

    ''' Compares each element from lexico_order_list to
    the raw_list. A counter keeps track of how many occurances of
    the same words. After each iteration in the nested loop, the
    value of counter is appended to the values_list list. The elements
    of the values_list has been mapped to each elements of
    the lexico_order_list.'''
    for i in range(0, len(lexico_order_list)):
        counter = 0
        for j in range(0, len(raw_list)):
            if lexico_order_list[i] == raw_list[j]:
                counter = counter + 1
        values.append(counter)

    # Calculates the frequency and adds it to frequency list.
    freq_list = []
    for i in range(0, len(values)):
        freq_list.append(values[i] / len(raw_list))

    ''' Organizes the information on the words, count and freq
    into a print_list as a list.(list inside list) '''
    print_list = [''] * len(lexico_order_list)
    for i in range(0, len(lexico_order_list)):
        word = raw_list[i]
        count = str(values[i])
        freq = str(round(freq_list[i], 3))
        print_list[i] = [word, count, freq]

    # Sends package to the writeFile()
    writeFile(print_list, fname)


def writeFile(print_list, fname):
    '''Writes the information passed by sort_analysis()
    to a file.'''
    fname = fname + '.out'
    inFile = open(fname, 'w')
    for i in print_list:
        inFile.write(' '.join(i))
        inFile.write('\n')
    inFile.close()


if __name__ == "__main__":
    openFile()
