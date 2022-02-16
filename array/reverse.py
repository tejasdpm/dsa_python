#Write a program to reverse an array or string



def reverseArray(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1

#driver function

A = [1, 2, 3, 4, 5, 6, 7]
print(A)
reverseArray(A, 0, 6)
print('Reversed array is')
print(A)


# using python slicing


def reverseList(A):
    print(A[::-1])


# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
print("Reversed list is")
reverseList(A)