def square(a):
    b = 1

    while b <= a:
        print(b ** 2, end=",")
        b += 1


def table(a):
    i = 1
    while i <= 10:
        # c = a * i
        print(a," x ",i," = ",a*i,)
        i += 1


if __name__ == '__main__':
    n = input("Enter a number ")
    # square(int(n))
    table(int(n))
