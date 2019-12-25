# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name = Jenish Patel
# Student ID: 1572027
# CMPUT 274, FALL 2019
# Weekly Assignment: Unfair Dice
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random
import math


def biased_rolls(prob_list, s, n):
    ''' The purpose of this function is to create and output a list
    containing the value of all n number of rolls in the order
    they were rolled.'''

    # Initalize sequence
    random.seed(s)
    output_list = [''] * n
    length = len(prob_list)

    ''' Calls mapping function n number of times and gets a integer
    indicating the roll when the dice is rolled.'''
    for i in range(0, n):
        roll = mapping(prob_list, length, random.random())
        output_list[i] = roll

    return output_list


def mapping(prob_list, length, prob):
    ''' The goal of this function is to mapped the probabilities from
    prob_list to a mapped_list containing a range which is "spaced"
    out according to the prob_list.'''
    mapped_list = [0] * (length + 1)
    new_prob = 0

    # Create a range to the appropriate numbers on the face of the die.
    for i in range(0, length):
        mapped_list[i+1] = mapped_list[i] + prob_list[i]

    '''The input arguement prob is the probability sent from biased_rolls
    will be compared to the elements of mapped_list and determines where prob
    fits inbetween two elements. new_prob acts like a counter and will keep
    track on which range the prob fits in and when prob fits into a range
    the value of new_prob will indicate the roll value.'''
    for i in range(0, len(mapped_list) - 1):
        if prob >= mapped_list[i] and prob < mapped_list[i + 1]:
            new_prob += 1
            return new_prob
        else:
            new_prob += 1


def draw_histogram(m, rolls, width):
    length = len(rolls)
    frequency_list = [0] * m
    dots_list = [0] * m

    ''' Creates a list containing the frequency of the occurences of
    rolls from rolls(list). A for loop will go through the rolls(list)
    and obtain the value of index j. That value will be a integer and
    it will serve as the index of frequency_list. So if value of rolls[j]
    is 5, then the 5 will be used as the index of frequency_list and its
    value will be accumulated by 1. '''
    for j in range(0, length):
        frequency_list[rolls[j]-1] += 1

    # Scale by which the histogram must be scaled by.
    scaleLength = (width / max(frequency_list))

    ''' The values of frequency_list is scaled and rounded to a integer.
    A histogram is printed by looping through m (faces of die), and print out
    the number of "*"s and then print the number of "."s.'''
    for i in range(0, m):
        frequency_list[i] = round(frequency_list[i] * scaleLength)
        dots_list[i] = width - frequency_list[i]
        print(i + 1, ":", "*"*frequency_list[i] + "." * dots_list[i])
