# program to find k'th smallest element

def kthsmall(arr, n, k):

    arr.sort()

    return arr[k-1]

#driver code

if __name__ =="__main__":
    arr = [1, 2, 3, 4, 45, 66]
    n = len(arr)
    k = 3
    print("K'th smallest element is", kthsmall(arr, n, k))



