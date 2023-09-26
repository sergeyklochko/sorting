def cycle_sort(arr):
    arr = arr[:]
    n = len(arr)
    swaps = 0

    for cycle_start in range(n - 1):
        item = arr[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        swaps += 1
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            swaps += 1

    return swaps, arr


my_list = [4, 3, 1, 2, 6, 8, 7, 5, 9]
swaps_needed, sorted_list = cycle_sort(my_list)
print(f"Минимальное количество перестановок для сортировки: {swaps_needed}")
print(f"Отсортированный список: {sorted_list}")
