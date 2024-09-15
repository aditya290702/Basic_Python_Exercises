def numsplit():
    num = 123
    digits = [int(digit) for digit in str(num)]
    return digits

def main():
    b = numsplit()
    print(b)

if __name__ == "__main__":
    main()
