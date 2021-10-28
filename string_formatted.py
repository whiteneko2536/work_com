def print_formatted(number):
    # your code goes here
    r = len(str(bin(number)[2:]))
    for N in range(1, number + 1):
        print("{} {} {} {}".format(str(N).rjust(r), str(oct(N)[2:]).rjust(r), (str(hex(N)[2:])).upper().rjust(r),
                                   str(bin(N)[2:]).rjust(r)))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)