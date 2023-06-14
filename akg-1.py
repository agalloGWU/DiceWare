#!/usr/bin/env python3

# First attempt at random password generator

import linecache
import json
import random # in case we're in testing mode
import requests

# TODO error checking on API call-
#   Did we get anything returned? (if not, maybe fall back to host PRN?)
#   Have we been rate limited (if so, report, and maybe fall back)
# TODO command line arguments for:
#   different input files
#   control capitalization (now defaults to initial caps)
#   number of words


def get_random_numbers(test=True):
    '''
    get random numbers from API
    for now, hardcoding values (URL, data type, array length, and block length)
    we need to ensure that we don't return values > the maximum number of lines in the file
    for now we're going to assume the file isn't bigger than 370105 (words_alpha.txt).  In the future,
    we may want to test this and set the value based on different values for different word lists
    we're going to modulo the random number with 370105
    :return: tuple of  ints
    '''
    if not test:        # because the API is rate limited, only run query if we're not testing
        response = requests.get("https://qrng.anu.edu.au/API/jsonI.php?length=4&type=hex16&size=3")
        jresponse = json.loads(response.text)
        ilist = []  # create an empty list to store the integers
        for item in jresponse['data']:
            intvalue = int(item, 16)
            if intvalue > 370105:
                newvalue = intvalue % 370105
                ilist.append(newvalue)
            else:
                ilist.append(intvalue)
    else:
        # ilist = [40136, 146960, 42647, 351612] == static data for testing
        ilist = []
        for i in range(0,4):
            ilist.append(random.randint(1,370105))
    return tuple(ilist)


def get_random_words(rnumbers):
    '''
    get words from list of words based on random numbers
    :param rnumbers: tuple of random numbers

    :return: Password!
    '''
    wordlist = []
    password = ''
    for i in range(0, 3):
        word = linecache.getline('words_alpha.txt', rnumbers[i]).split('\n')[0].capitalize()
        password += word
    return password


def main():
    random_ints = get_random_numbers()
    password = get_random_words(random_ints)
    print(password)


if __name__ == "__main__":
    main()




