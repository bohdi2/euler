from itertools import zip_longest

data_rows = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split('\n')[::-1]

xdata_rows = """
3
7 4
2 4 6
8 5 9 3""".split('\n')[::-1]


data = [list(map(int, x.split())) for x in data_rows]

def max_pairs(ns):
    result = [None] * (len(ns) - 1)

    for ii in range(len(ns)-1):
        result[ii] = max(ns[ii], ns[ii+1])

    return result

def add(ns, ms):
    return [x + y for x, y in zip_longest(ns, ms, fillvalue=0)]




if __name__ == "__main__":

    accumulator = []
    for row in data:
        #print(accumulator, "+", row, "=", add(accumulator, row))
        accumulator = add(accumulator, row)
        if len(accumulator) == 1:
            break
        accumulator = max_pairs(accumulator)

    print(accumulator)





    #max = iter(1, 0)

    #print(max)

