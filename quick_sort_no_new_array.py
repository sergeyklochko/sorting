def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


# Пример использования
arr = [38, 27, 43, 3, 9, 82, 10]
print("Исходный список:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Отсортированный список:", arr)


print(quick_sort([4, 9, 2, 7, 5]))
print(quick_sort([5, 8, 9, 4, 2, 9, 1, 8]))
