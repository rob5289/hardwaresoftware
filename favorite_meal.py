def meal_test(answer):
    if answer == 1:
           print("fried chicken yummy!")
    elif answer == 2:
        print("fried chicken yummy!")
    elif answer == 3:
        print("fried chicken yummy!")
    else:
         print("that is not an option!")

def main():
    print("which is your favorite meal?")
    print("1.chicken")
    print("2.burger")
    print("3.pizza)")
    answer = int(input())
    meal_test(answer)


if __name__ == '__main__':
    main()
