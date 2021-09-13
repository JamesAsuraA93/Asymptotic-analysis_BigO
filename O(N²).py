def display_all(lst):
    for item1 in lst:
        for item2 in lst:
            print([item1, item2], end=" ")
        print("\r")

def bubble_sorting():
    lst = [5,2,5,25,1,5,35,323,12,4,125,25,13,5,12,5,15,13,42]

    rng = len(lst)

    for i in range(rng):

        for j in range(0,len(lst)-1):

            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
            else:
                pass
        rng -= 1

    print(lst)
    
    
display_all([1, 2, 3, 4, 5])

bubble_sorting()
