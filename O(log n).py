def binary_search(lst, target, low, high):
    lst = sorted(lst, reverse=False)
    mid = low + high // 2
    if target == lst[mid]:
        return mid
    elif target < lst[mid]:
        # high = mid - 1
        return binary_search(lst, target, low, mid - 1)
    else:
        # target > lst[mid]:
        # low = mid + 1
        return binary_search(lst, target, mid - 1, high)


lst_data = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
point = 43
ans = binary_search(lst_data, point, 0, len(lst_data) - 1)
print(f"index of target({point}) is {ans}")
