# For use after vanitygen, you can run it with the command vanitygen -k -o addrs 1 > keys.txt
# This vectorizes and orders the key/address pairs according to their ascii character number

import pandas as pd

a = True
k = True
with open('keys.txt', "r", encoding='utf-16') as file:
    lines = file.readlines()
    for line in lines:
        address_dict = {}
        key_dict = {}
        if 'Address:' in line:
            l = line[9:]
            for j, i in enumerate(l):
                char = ord(i)
                if char != 10:
                    address_dict['Address Char {}'.format(j)] = char
            adf = pd.DataFrame.from_dict([address_dict])
            if a:
                adf.to_csv('addresses.csv', index=False)
                a = False
            else:
                adf.to_csv('addresses.csv', mode='a', index=False, header=False)
        elif 'Privkey:' in line:
            l = line[9:]
            for j, i in enumerate(l):
                char = ord(i)
                if char != 10:
                    key_dict['Key Char {}'.format(j)] = char
            kdf = pd.DataFrame.from_dict([key_dict])
            if k:
                kdf.to_csv('keys.csv', index=False)
                k = False
            else:
                kdf.to_csv('keys.csv', mode='a', index=False, header=False)
