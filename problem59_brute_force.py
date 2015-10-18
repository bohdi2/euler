#!/usr/bin/env python3

from itertools import cycle
import string


def read_cipher(filename):
    with open(filename, "r") as filestream:
        data = []
        for line in filestream:
            data += [int(s) for s in line.split(",")]
        return data


def ints_to_string(l):
    return "".join(map(chr, l))


def validate(text):
    return all(c in string.printable for c in text)


def key_generator():
    for a in range(128):
        print(a)
        for b in range(128):
            for c in range(128):
                yield [a, b, c]
    return


def decode(key, cipher):
    keys = cycle(key)
    return ints_to_string([next(keys) ^ n for n in cipher])

# Takes about 6 minutes to run

def main():
    cipher = read_cipher("p059_cipher.txt")

    for key in key_generator():
        s = decode(key, cipher)
        if "the " in s:
            print("%s: %s " % (key, s))


if __name__ == "__main__":
    main()
