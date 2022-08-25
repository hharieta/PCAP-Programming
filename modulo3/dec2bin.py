b = ""

def dec2bin(n):
    global b
    if n >= 1:
        dec2bin(n // 2 )
    b += str(n % 2)

def main():

    dec2bin(17)
    print(b)

if __name__ == '__main__':
    main()