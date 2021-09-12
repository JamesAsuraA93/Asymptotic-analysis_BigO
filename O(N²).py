def display_all(lst):
    for item1 in lst:
        for item2 in lst:
            print([item1, item2], end=" ")
        print("\r")


display_all([1, 2, 3, 4, 5])
