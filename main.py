if __name__ == '__main__':
    s = input()
    checker = [False] * 5
    for letter in s:
        if letter.isalnum():
            checker[0] = True
        if letter.isalpha():
            checker[1] = True
        if letter.isdigit():
            checker[2] = True
        if letter.islower():
            checker[3] = True
        if letter.isupper():
            checker[4] = True

    for x in checker:
        print(x)
