def quicksort(l: list):
    def quicksort_rec(l: list, i: int, j: int):
        if i < j:
            k = particion(l, i, j)
            quicksort_rec(l, i, k-1)
            quicksort_rec(l, k+1, j)
    quicksort_rec(l, 0, len(l) - 1)

def particion(l: list, i: int, j: int):
    x = l[j]
    k = i - 1
    for h in range(i, j):
        if l[h] <= x:
            k += 1
            l[h], l[k] = l[k], l[h]#intercambia(l, h, k)
    l[k+1], l[j] = l[j], l[k+1]#intercambia(l, k+1, j)
    return k+1
l = [3, 4, 1, 2, 5]
quicksort(l)
print(l)
