

def find_longest_subsequence(string):
    two_last_letters = []
    len_of_longest_subs = 0
    subs_counter = 0
    for i in range(string):
        asii_numbr = ord(string[i])
        if asii_numbr < 97 and asii_numbr > 122:
            subs_counter = 0
        else:
            if asii_numbr > ord(string[i-1]):
                subs_counter += 1
                len_of_longest_subs = max(len_of_longest_subs, subs_counter)
            else:
                subs_counter = 0
    return len_of_longest_subs
        print(asii_numbr)




if __name__ == '__main__':
    find_longest_subsequence('trial')

