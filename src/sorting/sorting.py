# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []

    while len(arrA) > 0 or len(arrB) > 0:
        if len(arrA) == 0:
            merged_arr += arrB
            return merged_arr
        elif len(arrB) == 0:
            merged_arr += arrA
            return merged_arr
        elif arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    midpt = int(len(arr)/2)
    l_arr = merge_sort(arr[:midpt])
    r_arr = merge_sort(arr[midpt:])

    return merge(l_arr, r_arr)

# # STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     pass


# def merge_sort_in_place(arr, l, r):
#     pass
