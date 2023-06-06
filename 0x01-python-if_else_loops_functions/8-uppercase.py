def uppercase(str):
    for c in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
        print("{:s}".format(ch), end='')

    print('\n', end="")
