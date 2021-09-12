def mergeSort(new_lst):
    if len(new_lst) > 1:
        mid = len(new_lst) // 2
        left = new_lst[:mid]
        right = new_lst[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                new_lst[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                new_lst[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            new_lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            new_lst[k] = right[j]
            j += 1
            k += 1


lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(lst)
print(lst)
