

def find_longest_subsequence(string):
    if not string:
        return 0, []
    if len(string) == 1:
        return 1, string
    two_last_letters = []
    len_of_longest_subs = 0
    subs_counter = 0
    for i in range(len(string)-1):
        asii_numbr = ord(string[i])
        asii_next_numb = ord(string[i+1])
        print(asii_numbr)
        if (asii_numbr < 97 or asii_numbr > 122) or (asii_next_numb < 97 or asii_next_numb > 122):
            subs_counter = 0
        else:
            if asii_numbr > asii_next_numb:

                subs_counter += 1
                # if i+1 == len(string)-1:
                #     subs_counter +=1

                len_of_longest_subs = max(len_of_longest_subs, subs_counter)
                two_last_letters = [chr(asii_numbr), chr(asii_next_numb)]

            else:

                subs_counter = 0



    print(two_last_letters)
    return len_of_longest_subs + 1, ''.join(two_last_letters)





if __name__ == '__main__':
    print(find_longest_subsequence('abbcdcba4566'))

