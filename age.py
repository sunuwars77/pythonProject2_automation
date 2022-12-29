def age(a):
    if a <= 15:
        print("you are child")
    elif a <= 20:
        print("you are teenage")
    else:
        print("you are old")


if __name__ == '__main__':
    n = input("enter your age")
    age(int(n))
