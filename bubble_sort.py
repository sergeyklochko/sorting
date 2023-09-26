def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)

    for i in range(n):
        # Флаг, чтобы определить, были ли какие-либо обмены на данной итерации
        swapped = False

        # Последние i элементов уже находятся на своих местах,
        # поэтому мы не будем их рассматривать
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего элемента, меняем их местами  # noqa
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Если на данной итерации не было обменов, массив уже отсортирован
        if not swapped:
            break

    return arr


# Пример использования:
my_list = [64, 25, 12, 22, 11]
sorted_list = bubble_sort(my_list)
print("Отсортированный массив:", sorted_list)
