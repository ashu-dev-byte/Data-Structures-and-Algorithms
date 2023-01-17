# Merge Sort

def merge(left, right):
    res = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])
    return res


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)


a = [56, 1, 3, 4, 5, 3, 3, 3, 67, 789, 3456, 1, 9, 6, 3, 34, 23, 0, -5, -10, -3, 57]
print(mergeSort(a))
