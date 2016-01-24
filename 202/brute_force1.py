
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def terminal(bounces):
    return (bounces+3)//2


def cycle(d):
    return -d % 3


def count(d, c):
    result = 0

    for ii in range(c, d, 3):
        if gcd(d, ii) == 1:
            result += 1

    return result


def laser(bounces):
    terminal_line = terminal(bounces)
    c = cycle(terminal_line)
    return count(terminal_line, c)


def main():
    for ii in [1000001, 12017639147]:
        print("laser", ii, "=>", laser(ii))

if __name__ == "__main__":
    main()





