

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
                print('j')
                subs_counter += 1
                print('counter:', subs_counter)
                len_of_longest_subs = max(len_of_longest_subs, subs_counter)
            else:
                print('n')
                subs_counter = 0
        print(len_of_longest_subs)
    return len_of_longest_subs





if __name__ == '__main__':
    print(find_longest_subsequence('trial'))

