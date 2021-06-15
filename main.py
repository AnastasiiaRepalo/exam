

def find_longest_subsequence(string):
    two_last_letters = []
    len_of_longest_subs = 0
    subs_counter = 0
    for i in range(len(string)-1):
        asii_numbr = ord(string[i])
        print(asii_numbr)
        if asii_numbr < 97 and asii_numbr > 122:
            subs_counter = 0
        else:
            if asii_numbr > ord(string[i+1]):

                subs_counter += 1

                len_of_longest_subs = max(len_of_longest_subs, subs_counter)
            else:

                subs_counter = 0
    return len_of_longest_subs + 1





if __name__ == '__main__':
    print(find_longest_subsequence('1t56ty6'))

