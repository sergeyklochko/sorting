def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[-1]
        less = [i for i in array[:-1] if i < pivot]
        greater = [i for i in array[:-1] if i > pivot]
        equal = [i for i in array if i == pivot]
        return quick_sort(less) + equal + quick_sort(greater)


print(quick_sort([4, 9, 2, 7, 5]))
print(quick_sort([5, 8, 9, 4, 2, 9, 1, 8]))
