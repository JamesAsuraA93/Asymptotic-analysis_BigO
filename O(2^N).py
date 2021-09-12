def display_recursive(number):
    if number == 0:
        return 0
    else:
        print(2 ** number)
        display_recursive(number - 1)


display_recursive(5)
