#!/usr/bin/env python3
'''
Andreck Soto 
PS ID: 1619873
COSC 3371 - Homework 1
'''

import sys
import traceback
from Crypto.Cipher import AES


# BEGIN SOLUTION
# please import only standard modules and make sure that your code compiles and runs without unhandled exceptions
# END SOLUTION


def problem_1():
    with open("cipher1.bin", "rb") as cipher_file:
        cipher_text = cipher_file.read()

    # BEGIN SOLUTION
    key = bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    iv = bytes([0] * 16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = cipher.decrypt(cipher_text)

    # END SOLUTION

    with open("plain1.txt", "wb") as plain_file:
        plain_file.write(plain_text)


def problem_2():
    with open("cipher2.bin", "rb") as cipher_file:
        cipher_text = cipher_file.read()

    # BEGIN SOLUTION
    modified_cipher_text = cipher_text[:]
    plain_text = modified_cipher_text

    key = bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    iv = bytes([0] * 16)

    block1 = cipher_text[:16]
    block2 = cipher_text[16:32]
    block3 = cipher_text[32:]
    cipher = AES.new(key, AES.MODE_CBC, iv)

    #msg = block1+block2+block3
    #msg = block2+block1+block3
    msg = block3+block2+block1

    plain_text = cipher.decrypt(msg)
    # END SOLUTION

    with open("plain2.txt", "wb") as plain_file:
        plain_file.write(plain_text)


def problem_3():
    with open("cipher3.bmp", "rb") as cipher_file:
        cipher_bmp = cipher_file.read()
    with open("msg3.bmp", "rb") as message_file:
        other_bmp = message_file.read()

    # BEGIN SOLUTION
    header = bytearray(other_bmp[:3000])
    modified_cipher_bmp = header + cipher_bmp[3000:]

    # END SOLUTION

    with open("cipher3_modified.bmp", "wb") as modified_cipher_file:
        modified_cipher_file.write(modified_cipher_bmp)


def problem_4():
    with open("plain4A.txt", "rb") as plain_file:
        plain_text_a = plain_file.read()
    with open("cipher4A.bin", "rb") as cipher_file:
        cipher_text_a = cipher_file.read()
    with open("cipher4B.bin", "rb") as cipher_file:
        cipher_text_b = cipher_file.read()

    # BEGIN SOLUTION

    def byteXOR (bf1,bf2):
        return(bytes([_a ^ _b for _a,_b in zip(bf1,bf2)]))
        
    xor1 = byteXOR(plain_text_a, cipher_text_a)
    xor2 = byteXOR(xor1, cipher_text_b)


    # END SOLUTION

    with open("plain4B.txt", "wb") as plain_file:
        plain_file.write(xor2)


def problem_5():
    with open("cipher5.bin", "rb") as cipher_file:
        cipher_text = cipher_file.read()

    # BEGIN SOLUTION
    #DAY
    for i in  range (1,13):
        #MONTH
        for j in  range (1,32):
            #YEARS
            for k in range (0,100):
                iv = bytes([0] * 16)
                key = bytes([i,j,k,0,0,0,0,0,0,0,0,0,0,0,0,0])
                cipher = AES.new(key, AES.MODE_CBC, iv)
                try:
                    cipher_text = cipher.decrypt(cipher_text).decode("utf-8")
                    cipher_text =  str.encode(cipher_text)
                except Exception:
                            pass
    plain_text = cipher_text


    # END SOLUTION

    with open("plain5.txt", "wb") as plain_file:
        plain_file.write(plain_text)


def main():
    try:
        problem_1()
        problem_2()
        problem_3()
        problem_4()
        problem_5()

    except Exception:
        print("Exception:")
        traceback.print_exc(file=sys.stdout)


if __name__ == "__main__":
    main()
