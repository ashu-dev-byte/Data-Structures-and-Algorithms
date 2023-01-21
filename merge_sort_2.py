# Merge Sort

def merge(arr, left, right, mid):
    res = [0] * (right - left + 1)
    i, j, k, c = left, mid + 1, 0, 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            res[k] = arr[i]
            i += 1
        else:
            res[k] = arr[j]
            j += 1
            c += (mid + 1) - i
        k += 1

    while i <= mid:
        res[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        res[k] = arr[j]
        k += 1
        j += 1

    arr[left:right + 1] = res

    return c


def merge_sort(arr, left, right):
    if left >= right:
        return 0

    c = 0
    mid = (left + right) // 2
    c += merge_sort(arr, left, mid)
    c += merge_sort(arr, mid + 1, right)
    c += merge(arr, left, right, mid)

    return c
  
  # ===========================================================================
  def merge(arr, left, mid, right):
    res = [0] * (right - left + 1)
    i, j, k = left, mid + 1, 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            res[k] = arr[i]
            i += 1
        else:
            res[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        res[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        res[k] = arr[j]
        k += 1
        j += 1

    arr[left:right + 1] = res


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


a = [5, 3, 2, 1, 4]
merge_sort(a, 0, len(a) - 1)
print(a)
