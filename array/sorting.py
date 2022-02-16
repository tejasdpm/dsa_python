# Sort an array of 0s, 1s and 2s

# Utility function to print contents of an array
def printArr(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


# Function to sort the array of 0s, 1s and 2s
def sortArr(arr, n):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0

    # Count the number of 0s, 1s and 2s in the array
    for i in range(n):
        if arr[i] == 0:
            cnt0 += 1

        elif arr[i] == 1:
            cnt1 += 1

        elif arr[i] == 2:
            cnt2 += 1

    # Update the array
    i = 0

    # Store all the 0s in the beginning
    while (cnt0 > 0):
        arr[i] = 0
        i += 1
        cnt0 -= 1

    # Then all the 1s
    while (cnt1 > 0):
        arr[i] = 1
        i += 1
        cnt1 -= 1

    # Finally all the 2s
    while (cnt2 > 0):
        arr[i] = 2
        i += 1
        cnt2 -= 1

    # Print the sorted array
    printArr(arr, n)


# Driver code

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n = len(arr)

sortArr(arr, n)


# Python program to sort an array with
# 0, 1 and 2 in a single pass

# Function to sort array
def sort012(a, arr_size):
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return a


# Function to print array
def printArray(a):
    for k in a:
        print(k, end=' ')


# Driver Program
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr_size = len(arr)
arr = sort012(arr, arr_size)
print("Array after segregation :", )
printArray(arr)



