import sys
import os.path


class Deck:

    '''
    Stores playing cards
    '''
    def __init__(self, cards):
        # Intializes attribute deck to object self.
        self.__deck = list(cards)

    def deal(self):
        ''' Deals out the top card in the deck. In this case the top card
        is index 0 of self.__deck. As it returns the first (top) card in
        the deck, it removes that card from the deck, simulating a real card
        game. '''
        if len(self.__deck) == 0:
            exit()
        else:
            dealt_card = self.__deck[0]
            self.__deck.remove(self.__deck[0])
            return dealt_card

    def validate(self):
        ''' Validates the deck by testing if the deck has 52 cards, if the
        cards are not duplicating and if they are any invalid cards in the deck.'''
        suits_list = ['S', 'D', 'C', 'H']
        rank_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

        ''' Checks for invalid cards by spliting of the each element from list
        (self.__deck) into two characters, the first character 'r' and 's'
        characters, represents the rank and suit of card respectively. The 'r' and 's' is
        compared with a list, which has predetermined values of the valid characters.
        It returns False if the 'r' or 's' does not match up with the predetermined list.'''

        # Checks for numbers of cards in deck
        if (len(self.__deck)) != 52:
            return (False, 'Incomplete Deck')

        # Checks for invalid cards in the deck
        for i in range(0, len(self.__deck)):
            r_s_list = list(str(self.__deck[i]))
            r = str(r_s_list[0])
            s = str(r_s_list[1])
            if (r in rank_list) is False:
                return (False, "Card {0} is not a valid card.".format(self.__deck[i]))
            if (s in suits_list) is False:
                return (False, "Card {0} is not a valid card.".format(self.__deck[i]))

        # Checks for duplicate cards in the deck
        copy_deck = self.__deck
        counter = 0
        for i in range(0, len(self.__deck)):
            counter = 0
            for j in range(0, len(self.__deck)):
                if self.__deck[j] == self.__deck[i]:
                    counter += 1
            if counter > 1:
                return (False, "Deck contains duplicate cards")
        if counter == 1:
            return(True, '')

        print(len(self.__deck))

    def __str__(self):
        # Returns a custom string with the cards in the deck.
        output_string = '-'.join(self.__deck)
        return output_string


def high_card_draw(deck):
    ''' Runs a game which simulates two players grabbing one card from the
    deck and comparing whose card is 'higher' than the other. '''
    player = [0, 0]
    dealer = [0, 0]
    i = 0
    while True:
        i += 1
        player = list(deck.deal())
        dealer = list(deck.deal())
        returned_list = format_non_int(player, dealer)
        if returned_list[0] > returned_list[1]:
            print('Round', i, ': Player Wins!')
        if returned_list[0] < returned_list[1]:
            print('Round', i, ': Dealer Wins!')
        if returned_list[0] == returned_list[1]:
            print('Round', i, ': Tie!')


def format_non_int(player, dealer):
    ''' For cards that have T,J,Q,K has their rank, the function turns them
    into numerically values.'''
    if player[0] == 'T':
        player[0] = 10
    if dealer[0] == 'T':
        dealer[0] = 10
    if player[0] == 'J':
        player[0] = 11
    if dealer[0] == 'J':
        dealer[0] = 11
    if player[0] == 'Q':
        player[0] = 12
    if dealer[0] == 'Q':
        dealer[0] = 12
    if player[0] == 'K':
        player[0] = 13
    if dealer[0] == 'K':
        dealer[0] = 13
    if player[0] == 'A':
        player[0] = 14
    if dealer[0] == 'A':
        dealer[0] = 14

    # Converts the strings in the list into integer to keep consistency.
    player[0] = int(player[0])
    dealer[0] = int(dealer[0])

    return_list = [player[0], dealer[0]]

    return return_list


def openFile():
    # Opens and read the data from a user inputed file.
    fname = commandInput()
    cards_list = []

    fid = open(fname, 'r+')
    for line in fid:
        line = line.strip('\n')
        cards_list.append(line)

    while '' in cards_list:
        cards_list.remove('')

    for i in range(0, len(cards_list)):
        cards_list[i] = cards_list[i].upper()

    return cards_list


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


def validation_response(deck):
    # Returns validility of the deck
    returned_list = deck.validate()
    if returned_list[0] is not True:
        print(returned_list[1])
        exit()
    else:
        return returned_list


if __name__ == "__main__":
    # Runs the program

    cards_list = openFile()
    deck = Deck(cards_list)
    validation_response(deck)

    print(deck)

    high_card_draw(deck)
